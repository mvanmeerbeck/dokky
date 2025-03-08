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

def detect_numbers(image):
    enhanced_image = enhance_contrast(image)
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

img = cv2.imread("tmp/level.jpg", 0)
cropped_img = crop_text_region(img)

detect_numbers(cropped_img)