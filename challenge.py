import subprocess
import cv2
import numpy as np
import time
from challengedata import (
    challenge_item_templates,
    challenge_list_item,
    histoire_sans_fin_template,
    zenis_template
)

zenis_template = cv2.imread("assets/challenge/zenis.jpg", cv2.IMREAD_GRAYSCALE)

objets_template = cv2.imread('./assets/challenge/objets.jpg', cv2.IMREAD_GRAYSCALE)

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

        zenis_match = match_template(image, zenis_template)

        if zenis_match['confidence'] >= 0.95:
            print("Zenis found!")
            tap("500", "1000")
            continue

        for template in challenge_item_templates:
            matched = match_and_tap(image, template)

            if matched:
                break

        if matched:
            continue

        objets_match = match_template(image, objets_template)

        if objets_match['confidence'] >= 0.95:
            print("Objects found!")
            tap("500", "1250")
            continue

        histoire_sans_fin_match = match_template(image, histoire_sans_fin_template)

        if histoire_sans_fin_match['confidence'] >= 0.95:
            print("Histoire sans fin found!")
            challenge_list_item_match = match_template(image, challenge_list_item)

            if challenge_list_item_match['confidence'] >= 0.95:
                print("Challenge list item found!")
                center_x = challenge_list_item_match['top_left'][0] + challenge_list_item_match['width'] // 2
                center_y = challenge_list_item_match['top_left'][1] + challenge_list_item_match['height'] // 2
                tap(str(center_x), str(center_y))
            else:
                print("No challenge list item found! Swiping...")
                swipe("254", "1561", "254", "1444")