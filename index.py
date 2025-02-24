import subprocess
import cv2
import numpy as np
import time
import datetime
import scenarios
import keyboard  # Add this import

def test_adb_connection():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if "List of devices attached" in result.stdout:
        print("Connected to ADB successfully!")
    else:
        print("Failed to connect to ADB.")

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

def match_template(image, template_path):
    template = cv2.imread(template_path, 0)
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = template.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, 255, 2)
    return image, max_val, top_left, w, h

def tap(x , y):
    subprocess.run(["adb", "shell", "input", "tap", x, y])

def match_and_tap(template):
    matched_image, confidence, top_left, w, h = match_template(image, template)
    print(f"template: {template}, confidence: {confidence}")
    if confidence > 0.85:
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        tap(str(center_x), str(center_y))

        return True
    else:
        print("Confidence is below threshold, not sending ADB command.")    

    return False

def start_app(package_name):
    subprocess.run(["adb", "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"])

def is_app_running(package_name):
    result = subprocess.run(["adb", "shell", "pidof", package_name], capture_output=True, text=True)
    return result.stdout.strip() != ""

def is_app_in_foreground(package_name):
    result = subprocess.run(["adb", "shell", "dumpsys", "window", "windows"], capture_output=True, text=True)
    return package_name in result.stdout

if __name__ == "__main__":
    test_adb_connection()
    package_name = "com.bandainamcogames.dbzdokkanww"
    if not is_app_running(package_name):
        start_app(package_name)
    elif not is_app_in_foreground(package_name):
        print(f"{package_name} is not in the foreground.")
    else:
        print(f"{package_name} is already running and in the foreground.")

    selected_scenario = scenarios.select_scenario(scenarios.SCENARII)
    paused = False  # Add this variable

    while True:
        if keyboard.is_pressed('p'):  # Check if 'p' is pressed
            paused = not paused
            if paused:
                print("Paused")
            else:
                print("Unpaused")
            time.sleep(1)  # Prevent rapid toggling

        if not paused:
            image = take_screenshot()

            templates = selected_scenario
            matched = False

            for template in templates:
                matched = match_and_tap(template)
                if matched:
                    break

        time.sleep(5)