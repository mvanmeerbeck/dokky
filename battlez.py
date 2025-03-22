import subprocess
import cv2
import numpy as np
import time
from battlezdata import (
    battle_z_loading,
    battle_z_cancel,
    battle_z_item_back,
    battle_z_item_templates,
    battle_z_item_new_enemy,
    battle_z_list,
    battle_z_items_image,
    battle_z_items_data,
    battle_z_item_level_image,
    battle_z_list_level_image,
    battle_z_item_next_level
)

# TODO si confidence < 0.9 back to list si level > 31

def take_screenshot():
    name = f"./tmp/screenshot.jpg"
    pipe = subprocess.Popen("adb shell screencap -p",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    gray_image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_GRAYSCALE)

    cv2.imwrite(name, gray_image)

    return gray_image

def match_template(image, template):
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = template.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    #cv2.rectangle(image, top_left, bottom_right, 255, 2)
    return {
        'image': image,
        'confidence': max_val,
        'top_left': top_left,
        'width': w,
        'height': h
    }

def crop_image(image, top_left, width, height):
    cropped_image = image[top_left[1]:top_left[1] + height, top_left[0]:top_left[0] + width]
    return cropped_image

def tap(x , y):
    subprocess.run(["adb", "shell", "input", "tap", x, y])

def swipe(x1, y1, x2, y2):
    subprocess.run(["adb", "shell", "input", "swipe", x1, y1, x2, y2])

def get_battle_z_item_by_height(height):
    index = height // 117
    keys = list(battle_z_items_data.keys())
    if index < len(keys):
        return keys[index], battle_z_items_data[keys[index]]
    return None

def get_battle_z_level_by_height(height, base_height):
    return (height // base_height) + 1

def match_and_tap(image, template):
    match = match_template(image, template)

    if match['confidence'] > 0.85:
        center_x = match['top_left'][0] + match['width'] // 2
        center_y = match['top_left'][1] + match['height'] // 2
        tap(str(center_x), str(center_y))

        return True
    return False

if __name__ == "__main__":
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if "List of devices attached" in result.stdout:
        print("Connected to ADB successfully!")
    else:
        print("Failed to connect to ADB.")

    current_item  = None
    current_key  = None

    while True:
        time.sleep(1)
        image = take_screenshot()
        matched = False

        battle_z_loading_match = match_template(image, battle_z_loading)
        if battle_z_loading_match['confidence'] >= 0.85:
            print("Loading...")
            time.sleep(2)
            continue

        battle_z_cancel_match = match_template(image, battle_z_cancel)

        if current_key != None and battle_z_cancel_match['confidence'] >= 0.95:
            print("Cancel detected")
            cv2.imwrite(f"./tmp/cancel.jpg", image)

            battle_z_items_data[current_key]['skip'] = True
            center_x = battle_z_cancel_match['top_left'][0] + battle_z_cancel_match['width'] // 2
            center_y = battle_z_cancel_match['top_left'][1] + battle_z_cancel_match['height'] // 2
            tap(str(center_x), str(center_y))
            continue

        for template in battle_z_item_templates:
            matched = match_and_tap(image, template)

            if matched:
                break

        if matched:
            continue

        battle_z_item_next_level_match = match_template(image, battle_z_item_next_level)
        if battle_z_item_next_level_match['confidence'] >= 0.85:
            if current_item != None:
                current_item['skip'] = False
            center_x = battle_z_item_next_level_match['top_left'][0] + battle_z_item_next_level_match['width'] // 2
            center_y = battle_z_item_next_level_match['top_left'][1] + battle_z_item_next_level_match['height'] // 2
            tap(str(center_x), str(center_y))
            time.sleep(1)
            continue

        battle_z_item_new_enemy_match = match_template(image, battle_z_item_new_enemy)

        if battle_z_item_new_enemy_match['confidence'] >= 0.85:
            battle_z_item_level = crop_image(image, (435,1540), 220, 105)
            cv2.imwrite(f"./tmp/item-level.jpg", battle_z_item_level)

            battle_z_item_level_match = match_template(battle_z_item_level, battle_z_item_level_image)
            item_level = get_battle_z_level_by_height(battle_z_item_level_match['top_left'][1], 105)
            print(battle_z_item_level_match)
            print(f"Item level: {item_level}")            

            if current_item != None and current_item['skip'] == False and item_level < current_item['level_target'] and battle_z_item_level_match['confidence'] >= 0.93:
                print("New enemy detected")
                center_x = battle_z_item_new_enemy_match['top_left'][0] + battle_z_item_new_enemy_match['width'] // 2
                center_y = battle_z_item_new_enemy_match['top_left'][1] + battle_z_item_new_enemy_match['height'] // 2
                tap(str(center_x), str(center_y))
            else:
                print("Back to list")
                match_and_tap(image, battle_z_item_back)

            continue

        battle_z_list_match = match_template(image, battle_z_list)

        if battle_z_list_match['confidence'] >= 0.95:
            print("On the Battle-Z list screen")

            battle_z_list_item_image = crop_image(image, (254,1561), 755, 117)

            battle_z_list_item_image_match = match_template(battle_z_list_item_image, battle_z_items_image)
            print(f"Battle-Z items confidence: {battle_z_list_item_image_match['confidence']} at {battle_z_list_item_image_match['top_left']} with size {battle_z_list_item_image_match['width']}x{battle_z_list_item_image_match['height']}")

            if battle_z_list_item_image_match['confidence'] > 0.90:
                item_key, item_data = get_battle_z_item_by_height(battle_z_list_item_image_match['top_left'][1])
                print(f"Matched item: {item_data['description']} with confidence {battle_z_list_item_image_match['confidence']}")

                level_image = crop_image(image, (910,570), 100, 58)
                cv2.imwrite(f"./tmp/level.jpg", level_image)
                
                battle_z_list_level_match = match_template(level_image, battle_z_list_level_image)
                list_level = get_battle_z_level_by_height(battle_z_list_level_match['top_left'][1], 58)
                print(battle_z_list_level_match)
                print(f"Item level: {list_level}")

                if item_data['skip'] == False and list_level < item_data['level_target'] and battle_z_list_level_match['confidence'] >= 0.75:
                    print(f"Go farm {item_data['description']}, level {list_level} < {item_data['level_target']}")
                    current_item = item_data
                    current_key = item_key
                    tap(str(254), str(1561))
                else:
                    print(f"Skip: {item_data['skip']}, Current level {list_level}, Target level {item_data['level_target']} => skipping")
                    swipe("254", "1561", "254", "1444")
                    time.sleep(1)
            continue
