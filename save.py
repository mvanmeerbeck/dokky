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
from battlez import take_screenshot, crop_image, swipe, match_template, detect_numbers

next_level_image = cv2.imread("assets/battle-z/next-level.jpg", 0)
start_image = cv2.imread("assets/battle-z/start.jpg", 0)

if __name__ == "__main__":
    while True:
        level = int(input("Please enter the level: "))        
        image_color = take_screenshot()
        image = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

        battle_z_list_match = match_template(image, battle_z_list)

        if battle_z_list_match['confidence'] > 0.85:
            list_level_image = crop_image(image, (910,570), 100, 58)

            cv2.imwrite(f"./tmp/list-level/{level}.jpg", list_level_image)

        battle_z_item_new_enemy_match = match_template(image, battle_z_item_new_enemy)

        if battle_z_item_new_enemy_match['confidence'] > 0.85:
            item_level_image = crop_image(image, (435,1540), 220, 105)

            cv2.imwrite(f"./tmp/item-level/{level}.jpg", item_level_image)