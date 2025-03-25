import cv2
import numpy as np

def merge_images(images):
    total_height = sum(image.shape[0] for image in images)
    max_width = max(image.shape[1] for image in images)
    merged_image = np.zeros((total_height, max_width), dtype=np.uint8)

    current_y = 0
    for image in images:
        merged_image[current_y:current_y + image.shape[0], :image.shape[1]] = image
        current_y += image.shape[0]

    return merged_image

challenge_list_item = cv2.imread('assets/challenge/list-item.jpg', 0)
histoire_sans_fin_template = cv2.imread('assets/challenge/histoire-sans-fin.jpg', 0)
bataille_boss_template = cv2.imread('assets/challenge/bataille-boss.jpg', 0)
super_battle_road_template = cv2.imread('assets/challenge/super-battle-road.jpg', 0)
assemblee_dieux_template = cv2.imread('assets/challenge/assemblee-dieux.jpg', 0)
esprit_combatif_template = cv2.imread('assets/challenge/esprit-combatif.jpg', 0)
zenis_template = cv2.imread('assets/challenge/zenis.jpg', 0)
objets_template = cv2.imread('assets/challenge/objets.jpg', 0)

challenge_item_templates = [
    cv2.imread("assets/challenge/KO.jpg", 0),
    cv2.imread("assets/challenge/move.jpg", 0),
    cv2.imread("assets/challenge/are-you-sure.jpg", 0),
    cv2.imread("assets/challenge/ok.jpg", 0),
    cv2.imread("assets/challenge/ok2.jpg", 0),
    cv2.imread("assets/challenge/start.jpg", 0),
    cv2.imread("assets/challenge/close.jpg", 0),
    cv2.imread("assets/challenge/rank-up.jpg", 0),
    cv2.imread("assets/challenge/ds.jpg", 0),
    cv2.imread("assets/challenge/passer.jpg", 0),
    cv2.imread('assets/challenge/super-3.jpg', 0),     
]