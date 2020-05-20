#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''utilities used to calculate chances when sitting on poker table'''

import os
import sys
import pyautogui as ag
import datetime
import json

poker_combinations = {
    'HC' : "High Card",
    '1P' : "One Pair",
    '2P' : "Two Pair",
    '3K' : "Three of a Kind",
    'ST' : "Straight",
    'FL' : "Flush",
    'FH' : "Full House",
    '4K' : "Four of a Kind",
    'SF' : "Straight Flush"
}

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

def clear_date_for_file(date):
    date = date.replace(' ', '_')
    date = date.replace(':', '_')
    date = date.replace('.', '_')
    return date[:-16]

def read_api_count(output = False):

    api_count_file_dir = get_script_path() + '//other//times_used_api_'
    api_count_date = clear_date_for_file(str(datetime.datetime.now()))
    api_count_file_full = api_count_file_dir + api_count_date + '.txt'

    if check_if_path_exists(api_count_file_full):
        file = open(api_count_file_full, 'r')
        times_api_used = file.read()
        file.close()
    else:
        file = open(api_count_file_full, 'w')
        file.write('0')
        file.close()
        times_api_used = 0

    if times_api_used is None or times_api_used == '':
        times_api_used = 1
    else:
        times_api_used = int(times_api_used)
    
    if output:
        print('Poker API was used:', times_api_used, 'times today')

    return times_api_used

def add_api_count():

    api_count_file_dir = get_script_path() + '//other//times_used_api_'
    api_count_date = clear_date_for_file(str(datetime.datetime.now()))
    api_count_file_full = api_count_file_dir + api_count_date + '.txt'

    file = open(api_count_file_full, 'w')
    times_api_used = read_api_count(False)
    times_api_used += 1
    file.write(str(times_api_used)) 
    file.close()

def normalize_card_color(card_color):

    if card_color == '♠':
        return 's'
    elif card_color == '♥':
        return 'h'
    elif card_color == '♦':
        return 'd'
    elif card_color == '♣':
        return 'c'
    else:
        return -1

def print_api_data(response, type):
    print('-----------------------')
    print('API DATA --- ', str(type).upper())
    print('-----------------------')
    
    if type == 'preflop':
        print('Cards in hand:', response['data']['hole_cards']['cards'][0]['full_name'], 'and', response['data']['hole_cards']['cards'][1]['full_name'])
        print('-----')
        print('Average hand on table:', response['data']['ranking']['average']['hand_name'], 'on', response['data']['ranking']['average']['rank_top_percent'], '%')
        print('--')
        for key, value in poker_combinations.items():
            print('Chance to finish with:', value, get_percentage_from_odds(response['data']['hit'][key]), '%')
        return

    elif type == 'flop' or type == 'turn':
        print('Average hand on table:', response['data']['me']['ranking']['average']['hand_name'], 'on', response['data']['me']['ranking']['average']['rank_top_percent'], '%')
        print('--')
        for key, value in poker_combinations.items():
            print('Chance to finish with:', value, get_percentage_from_odds(response['data']['me']['hit'][key]), '%')
        return

    elif type == 'river':
        print('Hand:', response['data']['me']['hand_name'])
        print('Win probability:', get_percentage_from_odds(response['data']['winning']['probability']), '%')
        return
    else:
        print('Bad input')

def get_percentage_from_odds(odds):
    percentage = float(odds) * 100
    return str(round(percentage, 3)) 

def convert_api_to_json(api_data):
    json_data = json.loads(api_data.text)
    return json_data

def check_for_10(card_number):
    if card_number == '10':
        return 'T'
    else:
        return card_number

def clear_screen():
    os.system('cls')

def check_if_path_exists(path):
    '''https://www.guru99.com/python-check-if-file-exists.html'''
    return os.path.exists(path)