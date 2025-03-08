import subprocess
import cv2
import numpy as np
import time
import datetime
import scenarios
import keyboard
import pytesseract

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

def detect_numbers(image):
    image = remove_color_background(image)
    cv2.imwrite(f"./tmp/enhancedcolor.jpg", image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    enhanced_image = enhance_contrast(image)
    enhanced_image = reduce_noise(enhanced_image)
    cv2.imwrite(f"./tmp/enhanced.jpg", enhanced_image)
    text = pytesseract.image_to_string(enhanced_image, config="--psm 6 outputbase digits")
    print(f"Detected text: {text}")
    
    try:
        text = int(text)
    except ValueError:  
        text = None

    return text

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

img = cv2.imread("tmp/enhanced0.jpg")
cropped_img = crop_text_region(img)

detect_numbers(cropped_img)