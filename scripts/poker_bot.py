#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''main script used to calculate chances when sitting on poker table'''


import scripts.util as util
import scripts.image_recognition as image_recog
import scripts.poker_strategies as ps
import time

def setup_cards():
    #import pyautogui as ag
    card_dirs = {}

    #create all the cards
    all_cards = []
    
    for card_number in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
        for card_color in ['♥', '♠', '♣', '♦']:
            basic_card = card_number + card_color
            
            #append to normal card array
            all_cards.append(basic_card)

            if card_color == '♥':
                card_color = 'hearts'
            elif card_color == '♣':
                card_color = 'clubs'
            elif card_color == '♦':
                card_color = 'diamonds'
            elif card_color == '♠':
                card_color = 'spades'

            directory = util.get_script_path() + u"\\images\\Cards\\table_cards" + u'\\' + card_number.lower() + '_' + card_color + '.png'
            directory = directory.replace('\\', "/")

            util.add_element_dict(card_dirs, basic_card, directory)

    poker_hands = {
    'royal_flush'       : 10,
    'straight_flush'    : 9,
    'four_same'         : 8,
    'full_house'        : 7,
    'flush'             : 6,
    'straight'          : 5,
    'three_same'        : 4,
    'two_pair'          : 3,
    'one_same'          : 2,
    'high_card'         : 1}


    return card_dirs, all_cards, poker_hands

card_directories, all_cards, poker_hands = setup_cards()

def bot():

    action = 'Preflop'
    #start detecting
    while True:
        
        #stages of hand:
        if action is None:
            quit()
        ## preflop
        elif action.lower() == 'preflop':
            preflop()
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['Flop', 'Restart', 'Quit'])

        ## flop
        elif action.lower() == 'flop':
            flop()
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['Turn', 'Restart', 'Quit'])

        ## turn
        elif action.lower() == 'turn':
            turn()
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['River', 'Restart', 'Quit'])
        
        ## river
        elif action.lower() == 'river':
            river()
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['Start Over', 'Restart', 'Quit'])
        

        elif action == 'Restart' or action == 'Start Over':
            action = 'Preflop'

        elif action == 'Quit':
            quit()

        else:
            quit("Don't press X... :D")
    
def preflop():
    #my_cards = image_recog.hand_cards(hand_card_directories) 
    my_cards = ['A♥', '2♥']
    util.print_line()
    print('[PREFLOP]: My Cards -', my_cards)
    ps.preflop(my_cards)
    util.print_line()

    return 

def flop():
    #cards = image_recog.table_cards(card_directories)
    cards = ['4♥', '8♦', '10♦']
    print('[FLOP]: Cards -', cards)
    util.print_line()
    ps.flop(cards)
    util.print_line()

    return 

def turn():
    #cards = image_recog.table_cards(card_directories)
    cards = ['4♥', '8♦', '10♦', 'A♦']
    util.print_line()
    print('[TURN]: Cards -', cards)
    ps.turn(cards)
    util.print_line()
    
    return

def river():
    #cards = image_recog.table_cards(card_directories)
    cards = ['4♥', '8♦', '10♦', 'A♦', '6♦']
    util.print_line()
    print('[RIVER]: Cards -', cards)
    ps.river(cards)
    util.print_line()
    
    return

def after_hand(table_cards, my_cards):
    table_cards = []
    my_cards = []
    return table_cards, my_cards

