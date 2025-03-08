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
    battle_z_cancel,
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
    gray_image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)

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

def reduce_noise(image):
    return cv2.fastNlMeansDenoising(image, None, 30, 7, 21)

def remove_specific_background(image, lower_color, upper_color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask_inv = cv2.bitwise_not(mask)
    image[mask != 0] = [0, 0, 0]
    return image

def remove_color_background(image):
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    image = remove_specific_background(image, lower_red1, upper_red1)
    
    lower_red2 = np.array([160, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    image = remove_specific_background(image, lower_red2, upper_red2)
    
    lower_red3 = np.array([10, 50, 50])
    upper_red3 = np.array([20, 255, 255])
    image = remove_specific_background(image, lower_red3, upper_red3)
    
    lower_red4 = np.array([170, 50, 50])
    upper_red4 = np.array([180, 255, 255])
    image = remove_specific_background(image, lower_red4, upper_red4)
    
    lower_red4 = np.array([12, 167, 250])
    upper_red4 = np.array([180, 255, 255])
    image = remove_specific_background(image, lower_red4, upper_red4)
    
    lower_yellow = np.array([15, 50, 50])
    upper_yellow = np.array([35, 255, 255])
    image = remove_specific_background(image, lower_yellow, upper_yellow)
    
    return image

def crop_text_region(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200, 255)
    
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Contours: {len(contours)}")
    if contours:
        x, y, w, h = cv2.boundingRect(contours[0])
        for c in contours:
            x1, y1, w1, h1 = cv2.boundingRect(c)
            x = min(x, x1)
            y = min(y, y1)
            w = max(w, x1 + w1 - x)
            h = max(h, y1 + h1 - y)

        padding = 2
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(image.shape[1] - x, w + 2 * padding)
        h = min(image.shape[0] - y, h + 2 * padding)
        cropped_image = image[y:y + h, x:x + w]
        return cropped_image
    else:
        return image

def detect_numbers(image, colored=False):
    cv2.imwrite(f"./tmp/enhanced0.jpg", image)
    image = crop_text_region(image)
    if colored:
        image = remove_color_background(image)
        cv2.imwrite(f"./tmp/enhanced1b.jpg", image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"./tmp/enhanced1.jpg", image)
    image = enhance_contrast(image)
    cv2.imwrite(f"./tmp/enhanced2.jpg", image)
    image = reduce_noise(image)
    cv2.imwrite(f"./tmp/enhanced3.jpg", image)
    text = pytesseract.image_to_string(image, config="--psm 6 outputbase digits")
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
        return keys[index], battle_z_items_data[keys[index]]
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
    current_key  = None
    back_to_list = False
    check_enemy_level = True

    while True:
        print(current_item)
        time.sleep(2)
        image_color = take_screenshot()
        image = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
        matched = False

        battle_z_loading_match = match_template(image, battle_z_loading)
        if battle_z_loading_match['confidence'] >= 0.85:
            print("Loading...")
            time.sleep(2)
            continue

        battle_z_cancel_match = match_template(image, battle_z_cancel)

        if battle_z_cancel_match['confidence'] >= 0.85:
            back_to_list = True
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

        battle_z_item_new_enemy_match = match_template(image, battle_z_item_new_enemy)

        if battle_z_item_new_enemy_match['confidence'] >= 0.85:
            battle_z_item_level = crop_image(image_color, (435,1540), 220, 105)
            cv2.imwrite(f"./tmp/item-level.jpg", battle_z_item_level)

            item_level = detect_numbers(battle_z_item_level, True)

            if item_level != None and current_item != None and current_item['skip'] == False and item_level < current_item['level_target']:
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

            if battle_z_list_item_image_match['confidence'] > 0.95:
                item_key, item_data = get_battle_z_item_by_height(battle_z_list_item_image_match['top_left'][1])
                print(f"Matched item: {item_data['description']} with confidence {battle_z_list_item_image_match['confidence']}")

                level_image = crop_image(image, (910,570), 100, 58)
                cv2.imwrite(f"./tmp/level.jpg", level_image)

                level = detect_numbers(level_image)

                if level != None and item_data['skip'] == False and level < item_data['level_target']:
                    print(f"Go farm {item_data['description']}, level {level} < {item_data['level_target']}")
                    current_item = item_data
                    current_key = item_key
                    tap(str(254), str(1561))
                else:
                    print(f"Skip: {item_data['skip']}, Current level {level}, Target level {item_data['level_target']} => skipping")
                    swipe("254", "1561", "254", "1444")
            continue
