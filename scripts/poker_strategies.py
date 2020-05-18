#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''poker algorithms script used to calculate chances when sitting on poker table'''

import scripts.util as util


def preflop(cards, players):
    
    first_card_number, first_card_color = util.split_color_number(cards[0])
    second_card_number, second_card_color = util.split_color_number(cards[1])

    #convert 10 to T
    if first_card_number == '10':
        first_card_number = 'T'
    if second_card_number == '10':
        second_card_number = 'T'

    if second_card_color == first_card_color:
        feature = 'suited'
    elif first_card_number == second_card_number:
        feature = 'pocket_pair'
    else:
        feature = 'others'

    cards = [first_card_number, second_card_number, first_card_color, second_card_color]

    #generate flops and percentage
    generate_pre_flops(mode = feature, cards = cards)
       
    return

def flop(cards, my_cards, players):
    check_for_possible_combos(cards, my_cards, cards_on_table = players)
    return

def turn(cards, my_cards, players):
    check_for_possible_combos(cards, my_cards, cards_on_table = players)
    return
    
def river(cards, my_cards, players):
    check_for_possible_combos(cards, my_cards, cards_on_table = players)
    return

def generate_pre_flops(mode, cards): 
    '''https://www.preflophands.com/'''
    if mode == 'suited':
        pre_flops = {
            "AK" : 4,
            "AQ" : 6,
            "KQ" : 7,
            "AJ" : 8,
            "KJ" : 9,
            "AT" : 12,
            "QJ" : 13,
            "KT" : 14,
            "QT" : 15,
            "JT" : 16,
            "A9" : 19,
            "K9" : 22,
            "T9" : 23,
            "A8" : 24,
            "Q9" : 25,
            "J9" : 26,
            "A5" : 28,
            "A7" : 30,
            "A4" : 32,
            "A3" : 33,
            "A6" : 34,
            "K8" : 37,
            "T8" : 38,
            "A2" : 39,
            "98" : 40,
            "J8" : 41,
            "Q8" : 43,
            "K7" : 44,
            "87" : 48,
            "K6" : 53,
            "97" : 54,
            "K5" : 55,
            "76" : 56,
            "T7" : 57,
            "K4" : 58, 
            "K3" : 59,
            "K2" : 60,
            "Q7" : 61,
            "86" : 62,
            "65" : 63,
            "J7" : 64,
            "54" : 65,
            "Q6" : 66,
            "75" : 67,
            "96" : 68,
            "Q5" : 69,
            "64" : 70,
            "Q4" : 71,
            "Q3" : 72,
            "T6" : 74,
            "Q2" : 75,
            "53" : 77,
            "J6" : 79,
            "J5" : 82,
            "43" : 84,
            "74" : 85,
            "J4" : 86,
            "J3" : 87,
            "95" : 88,
            "J2" : 89,
            "63" : 90,
            "52" : 92,
            "T5" : 93,
            "84" : 94,
            "T4" : 95,
            "T3" : 96,
            "42" : 97,
            "T2" : 98,
            "73" : 103,
            "32" : 105,
            "94" : 106,
            "93" : 107,
            "62" : 110,
            "92" : 111,
            "83" : 116,
            "82" : 118,
            "72" : 120 }

    elif mode == 'pocket_pair':
        pre_flops = {
            "AA" : 1,
            "KK" : 2,
            "QQ" : 3,
            "JJ" : 5,
            "TT" : 10,
            "99" : 17,
            "88" : 21,
            "77" : 29,
            "66" : 36,
            "55" : 46,
            "44" : 50,
            "33" : 51,
            "22" : 52 
            }

    elif mode == 'others':
        pre_flops = {
            "AK" : 11,
            "AQ" : 18,
            "KQ" : 20,
            "AJ" : 27,
            "KJ" : 31,
            "QJ" : 35,
            "AT" : 42,
            "KT" : 45,
            "JT" : 47,
            "QT" : 49,
            "T9" : 73,
            "A9" : 76,
            "J9" : 80,
            "K9" : 81,
            "Q9" : 83, 
            "A8" : 91,
            "98" : 99,
            "T8" : 100,
            "A5" : 101,
            "A7" : 102,
            "A4" : 104,
            "J8" : 108,
            "A3" : 109,
            "K8" : 112,
            "A6" : 113,
            "87" : 114,
            "Q8" : 115,
            "A2" : 117,
            "97" : 119,
            "76" : 121,
            "K7" : 122,
            "65" : 123,
            "T7" : 124,
            "K6" : 125,
            "86" : 126,
            "54" : 127,
            "K5" : 128,
            "J7" : 129,
            "75" : 130,
            "Q7" : 131,
            "K4" : 132,
            "K3" : 133,
            "96" : 134,
            "K2" : 135,
            "64" : 136,
            "Q6" : 137,
            "53" : 138,
            "85" : 139,
            "T6" : 140,
            "Q5" : 141,
            "43" : 142,
            "Q4" : 143,
            "Q3" : 144,
            "74" : 145,
            "Q2" : 146,
            "J6" : 147,
            "63" : 148,
            "J5" : 149,
            "95" : 150,
            "52" : 151,
            "J4" : 152,
            "J3" : 153,
            "42" : 154,
            "J2" : 155,
            "84" : 156,
            "T5" : 157,
            "T4" : 158,
            "32" : 159,
            "T3" : 160,
            "73" : 161,
            "T2" : 162,
            "62" : 163,
            "94" : 164,
            "93" : 165,
            "92" : 166,
            "83" : 167,
            "82" : 168,
            "72" : 169 }

    find = cards[0] + cards[1]
    find2 = cards[1] + cards[0]

    ranking = pre_flops.get(find) 
    other_ranking = pre_flops.get(find2)

    if ranking is None and other_ranking is None:
        quit(ranking, 'and', other_ranking, 'not found???')
    
    elif ranking is None:
        ranking = other_ranking


    ranking = 168 - ranking
    percentage = round((ranking * 100) / 167, 2)\
    
    print('Preflop rating from other preflops: ', end= '')
    print(percentage, '% better', end = ' ')
    print('(' + str(ranking) + '/167)')


    return 
    
def check_for_possible_combos(cards = None, my_cards = None, cards_on_table = 3, players_in_table = 5):

    #TODO: ValueError: not enough values to unpack (expected 2, got 0)
    sort_cards(cards)

    if cards_on_table >= 3:
        flush(cards, cards_on_table)
        #check for royal flush
        #'A♦♣♠♥'
        # for card in cards:
        #     same_colour = 
        #print(cards_on_table)
    #elif cards_on_table >= 4:
    #     print(cards_on_table)

    #elif cards_on_table >= 5:
    #     print(cards_on_table)

    
    #check for royal flush
    #for 

def sort_cards(cards):

    sort_by = {
        'A' : 14,
        'K' : 13,
        'Q' : 12,
        'J' : 11,
        '10' : 10,
        '9' : 9,
        '8' : 8,
        '7' : 7, 
        '6' : 6,
        '5' : 5,
        '4' : 4,
        '3' : 3,
        '2' : 2
    }

    colors = []
    numbers = []
    new_cards = []

    for card in cards:
        
        color = util.get_card_color(card)
        colors.append(color)
        
        number = util.get_card_number(card)
        numbers.append(sort_by.get(number))

    numbers, colors = zip(*sorted(zip(numbers, colors)))

    for i in range(len(numbers)):
        #https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
        number = list(sort_by.keys())[list(sort_by.values()).index(numbers[i])]
        new_cards.append(str(number) + str(colors[i]))

    return new_cards

def straight(cards, card_count):
    #7♦ 8♦ 9♦
    return

def flush(cards, card_count):
    hearts = 0
    clubs = 0
    spades = 0
    diamonds = 0

    for card in cards:
        check = util.get_card_color(card)
        if check == '♥':
            hearts += 1
        elif check == '♣':
            clubs += 1
        elif check == '♠':
            spades += 1
        elif check == '♦':
            diamonds += 1
    
    color_max = max(hearts, clubs, diamonds, spades)

    #print(color_max)
    return
    
def three_of_a_kind(cards, card_count):
    return
