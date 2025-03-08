import subprocess
import cv2
import numpy as np
import time
import datetime
import scenarios
import keyboard
import pytesseract
from battlezdata import (
    battle_z_loading,
    battle_z_item_back,
    battle_z_item_enemy_level_label,
    battle_z_item_infos_combat,
    battle_z_item_templates,
    battle_z_item_new_enemy,
    battle_z_list,
    battle_z_items_image,
    battle_z_items_data
)

def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
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

def enhance_contrast(image):
    thresh = cv2.threshold(image, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    return thresh

def crop_text_region(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200, 255)
    
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        # Add padding of 10 pixels around the detected text region
        padding = 10
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(image.shape[1] - x, w + 2 * padding)
        h = min(image.shape[0] - y, h + 2 * padding)
        cropped_image = image[y:y + h, x:x + w]
        return cropped_image
    else:
        return image

def detect_numbers(image):
    cropped_image = crop_text_region(image)
    enhanced_image = enhance_contrast(cropped_image)
    cv2.imwrite(f"./tmp/enhanced.jpg", enhanced_image)
    text = pytesseract.image_to_string(enhanced_image, config="--psm 6 outputbase digits")
    print(f"Detected text: {text}")
    
    try:
        text = int(text)
    except ValueError:  
        text = None

    return text

def crop_image(image, top_left, width, height):
    cropped_image = image[top_left[1]:top_left[1] + height, top_left[0]:top_left[0] + width]
    return cropped_image

def display_image_size(image):
    height, width = image.shape
    print(f"Image size: {width}x{height}")

def tap(x , y):
    subprocess.run(["adb", "shell", "input", "tap", x, y])

def swipe(x1, y1, x2, y2):
    subprocess.run(["adb", "shell", "input", "swipe", x1, y1, x2, y2])

def get_battle_z_item_by_height(height):
    index = height // 117
    keys = list(battle_z_items_data.keys())
    if index < len(keys):
        return battle_z_items_data[keys[index]]
    return None

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
    back_to_list = False
    check_enemy_level = True

    while True:
        time.sleep(2)
        image = take_screenshot()
        matched = False

        battle_z_loading_match = match_template(image, battle_z_loading)
        if battle_z_loading_match['confidence'] >= 0.85:
            print("Loading...")
            time.sleep(2)
            continue

        if back_to_list:
            battle_z_item_back_match = match_and_tap(image, battle_z_item_back)
            if battle_z_item_back_match:
                back_to_list = False
                continue

        if check_enemy_level == True:
            battle_z_item_enemy_level_label_match = match_template(image, battle_z_item_enemy_level_label)

            if battle_z_item_enemy_level_label_match['confidence'] >= 0.85:
                print("On the Battle-Z Infos Combat screen")

                battle_z_item_enemy_level = crop_image(image, (575,680), 70, 50)
                cv2.imwrite(f"./tmp/battle-z-item-enemy-level.jpg", battle_z_item_enemy_level)
                
                level = detect_numbers(battle_z_item_enemy_level)
                print(f"Level: {level}")

                if current_item == None or level >= current_item['level_target']:
                    print("retour list")
                    back_to_list = True
                
                check_enemy_level = False                    
                continue
            
            battle_z_item_infos_combat_match = match_and_tap(image, battle_z_item_infos_combat)

            if battle_z_item_infos_combat_match:
                continue

        for template in battle_z_item_templates:
            matched = match_and_tap(image, template)

            if matched:
                break

        if matched:
            continue

        battle_z_item_new_enemy_match = match_and_tap(image, battle_z_item_new_enemy)

        if battle_z_item_new_enemy_match:
            check_enemy_level = True
            continue

        battle_z_list_match = match_template(image, battle_z_list)

        if battle_z_list_match['confidence'] >= 0.95:
            print("On the Battle-Z list screen")

            battle_z_list_item_image = crop_image(image, (254,1561), 755, 117)

            battle_z_list_item_image_match = match_template(battle_z_list_item_image, battle_z_items_image)
            print(f"Battle-Z items confidence: {battle_z_list_item_image_match['confidence']} at {battle_z_list_item_image_match['top_left']} with size {battle_z_list_item_image_match['width']}x{battle_z_list_item_image_match['height']}")

            if battle_z_list_item_image_match['confidence'] > 0.95:
                item_data = get_battle_z_item_by_height(battle_z_list_item_image_match['top_left'][1])
                print(f"Matched item: {item_data['description']} with confidence {battle_z_list_item_image_match['confidence']}")

                level_image = crop_image(image, (910,570), 100, 58)
                cv2.imwrite(f"./tmp/level.jpg", level_image)

                level = detect_numbers(level_image)

                if level < item_data['level_target']:
                    print(f"Go farm {item_data['description']}, level {level} < {item_data['level_target']}")
                    current_item = item_data
                    tap(str(254), str(1561))
                else:
                    print(f"Level {level} >= {item_data['level_target']}, skipping")
                    swipe("254", "1561", "254", "1444")
            continue
