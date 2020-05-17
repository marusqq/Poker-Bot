#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''image recognition script used to calculate chances when sitting on poker table'''

import pyautogui as ag
import cv2
import numpy as np
from scripts.util import get_script_path

def table_cards(card_images):
    '''https://docs.opencv.org/3.1.0/d4/dc6/tutorial_py_template_matching.html'''
    cards = []
    accuracy = 0.99
    file_path = take_save_screenshot()

    table_image = read_image_and_change_to_gray(file_path)

    for key, value in card_images.items():

        card_to_find = cv2.imread(value[0], 0)
        res = cv2.matchTemplate(table_image,card_to_find,cv2.TM_CCOEFF_NORMED)
        
        card_found = np.where(res >= accuracy)
        if card_found[0].size > 0 or card_found[1].size > 0:
            cards.append(key)

    return cards

def read_image_and_change_to_gray(image_path):
    img_rgb = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    return img_gray

def take_save_screenshot():
    '''https://datatofish.com/screenshot-python/'''
    myScreenshot = ag.screenshot()
    file_path = get_script_path() + r'\images\screenshots\table.png'
    myScreenshot.save(file_path)
    return file_path