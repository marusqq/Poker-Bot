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
            my_cards = preflop()
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['Flop', 'Restart', 'Quit', 'Rescan'])
            if action == 'Rescan':
                action = 'Preflop'

        ## flop
        elif action.lower() == 'flop':
            cards = flop(my_cards)
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['Turn', 'Restart', 'Quit', 'Rescan'])
            if action == 'Rescan':
                action = 'Flop'

        ## turn
        elif action.lower() == 'turn':
            cards = turn(my_cards, cards)
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['River', 'Restart', 'Quit', 'Rescan'])
            if action == 'Rescan':
                action = 'Turn'
        
        ## river
        elif action.lower() == 'river':
            river(my_cards, cards)
            #wait for user confirmation that flop is finished
            action = util.button_popup(
                text_to_show = 'Now at ' + action + '. Continue?', 
                title_to_show = '♠♥ Poker Face ♦♣',
                buttons_to_press = ['Start Over', 'Restart', 'Quit', 'Rescan'])
            if action == 'Rescan':
                action = 'River'
        

        elif action == 'Restart' or action == 'Start Over':
            action = 'Preflop'

        elif action == 'Quit':
            quit()

        else:
            quit("Don't press X... :D")
    
def preflop():
    _type = 'Hand'
    my_cards = input_cards(card_count = 2, type = _type)
    players = input_players(type = _type)
    #my_cards = ['A♥', '2♥']
    
    util.print_line()
    print('[PREFLOP]: My Cards -', my_cards)
    ps.preflop(my_cards, players)
    util.print_line(True)

    return my_cards

def flop(my_cards):
    _type = 'Flop'
    cards = input_cards(card_count = 3, type = _type)
    players = input_players(type = _type)
    #cards = ['4♥', '8♦', '10♦']
    
    util.print_line()
    print('[FLOP]: Cards -', cards)
    ps.flop(cards, my_cards, players)
    util.print_line(True)

    return cards

def turn(my_cards, cards):
    _type = 'Turn'
    cards = cards + input_cards(card_count = 1, type = _type)
    players = input_players(type = _type)

    #cards = ['4♥', '8♦', '10♦', 'A♦']
    
    util.print_line()
    print('[TURN]: Cards -', cards)
    ps.turn(cards, my_cards, players)
    util.print_line(True)
    
    return cards

def river(my_cards, cards):
    _type = 'River'
    cards = cards + input_cards(card_count = 1, type = _type)
    players = input_players(type = _type)
    #cards = ['4♥', '8♦', '10♦', 'A♦', '6♦']
    
    util.print_line()
    print('[RIVER]: Cards -', cards)
    ps.river(cards, my_cards, players)
    util.print_line(True)
    
    return

def after_hand(table_cards, my_cards):
    table_cards = []
    my_cards = []
    return table_cards, my_cards

def input_cards(card_count, type):

    cards = []
    while card_count > 0:
        card_number = \
        util.button_popup(
            text_to_show = type + ' Card Number:',
            title_to_show = '♠♥ Poker Face ♦♣',
            buttons_to_press = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'])

        card_color = \
        util.button_popup(
            text_to_show = type + ' Card Color:',
            title_to_show = '♠♥ Poker Face ♦♣',
            buttons_to_press = ['♠', '♥', '♦', '♣'])
        
        cards.append(card_number + card_color)
        card_count -= 1

    return cards
    
def input_players(type):
    players =  util.button_popup(
            text_to_show = type + ' Players playing:',
            title_to_show = '♠♥ Poker Face ♦♣',
            buttons_to_press = ['6', '5', '4', '3', '2', '1'])
    return players