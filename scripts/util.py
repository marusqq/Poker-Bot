#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''utilities used to calculate chances when sitting on poker table'''

import os
import sys
import pyautogui as ag

def add_element_dict(dict, key, value):
    '''https://stackoverflow.com/questions/33272588/appending-elements-to-an-empty-dictionary-of-lists-in-python'''
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

def get_script_path():
    '''https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory-with-python'''
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def button_popup(text_to_show, title_to_show, buttons_to_press):
    '''https://pyautogui.readthedocs.io/en/latest/msgbox.html'''
    chosen_option = ag.confirm(text=text_to_show, title=title_to_show, buttons=buttons_to_press)
    return chosen_option

def print_line(newline_at_end = False):
    if newline_at_end:
        print('--------------------------------------------------\n')
    else:
        print('--------------------------------------------------')
def split_color_number(cards):
    return cards[:-1].upper(), cards[-1:]

def get_card_number(card):
    return card[:-1].upper()

def get_card_color(card):
    return card[-1:]