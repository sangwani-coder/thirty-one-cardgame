# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:12:35 2021

@author: PZ
"""

def cardDeck():
    deck = []
    
    face_values =["A", "J", "K", "Q"]
    suit = ["H","S", "D", "C"]
    
    for suit in suit:
        for card in face_values:
            deck.append(card + suit)
            
        for card in range(2,11):
            deck.append(str(card) + suit)
            
    # shuffle(deck)
    return deck
deck = cardDeck()


hearts =['AH', 'JH', 'KH', 'QH', '2H', '3H', '4H', 
         '5H', '6H', '7H', '8H', '9H', '10H']
spades =['AS', 'JS', 'KS', 'QS', '2S', '3S', '4S',
         '5S', '6S', '7S', '8S', '9S', '10S']
diamonds = ['AD', 'JD', 'KD', 'QD', '2D', '3D', '4D',
            '5D', '6D', '7D', '8D', '9D', '10D'] 
clubs = ['AC', 'JC', 'KC', 'QC', '2C', '3C', 
         '4C', 
         '5C', '6C', '7C', '8C', '9C', '10C']

suits_dict = {'AH':11, 'JH':10, 'KH':10, 'QH':10, '2H':2, '3H':3, 
          '4H':4, '5H':5, '6H':6, '7H':7, '8H':8, '9H':9, '10H':10, 
          'AS':11,'JS':10, 'KS':10, 'QS':10, '2S':2, '3S':3, 
          '4S':4, '5S':5, '6S':6, '7S':7, '8S':8, '9S':9, '10S':10,
          'AD':11, 'JD':10, 'KD':10, 'QD':10, '2D':2, '3D':3, 
            '4D':4, '5D':5, '6D':6, '7D':7, '8D':8, '9D':9, '10D':10,
            'AC':11, 'JC':10, 'KC':10, 'QC':10, '2C':2,'3C':3, 
         '4C':4, '5C':5, '6C':6, '7C':7, '8C':8, '9C':9, '10C':10}

card_kind_dict = {"aces":["AH", "AS","AD","AC"],"twos":["2H","2S", "2D", "2C"],"threes":["3H","3S", "3D", "3C"],
             "fours":["4H","4S", "4D", "4C"],"fives":["5H","5S", "5D", "5C"], "six":["6H","6S", "6D", "6C"],
             "sevens":["7H", "7S","7D","7C"],"eights":["8H","8S", "8D", "8C"],"nines":["9H","9S", "9D", "9C"],
             "tens":["10H","10S", "10D", "10C"], "jacks":["JH","JS", "JD", "JC"], "kings":["KH","KS", "KD", "KC"],
             "queens":["QH","QS", "QD", "QC"]}




