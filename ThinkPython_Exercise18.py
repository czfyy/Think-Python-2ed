# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:00:32 2019

@author: czfyy
"""

import random

class Card:
    '''桥牌   suit：花色 rank：点数
    
    规则：花色 > 点数  （即 梅花3 < 方片2 ）
    -------------------------------------------
    花色大小依次递减
    Spades：黑桃       ↦    3
    Hearts：红心       ↦    2
    Diamonds：方片     ↦    1
    Clubs：梅花        ↦    0
    -------------------------------------------
    点数
    Ace       ↦    1
    2         ↦    2
    .              
    .
    .
    10        ↦    10
    Jack      ↦    11
    Queen     ↦    12
    King      ↦    13
    '''
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit=0, rank=2): #默认梅花2
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):#less than
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        return t1 < t2
        
class Deck:
    #一副纸牌
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        return self.cards.append(card)
    
    def move_cards(self, hand, num):
        for i in range(num):
            card = self.pop_card()
            hand.add_card(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort(reverse=True) #默认升序 reverse=False

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
    return None
    
def main():
    
    hand = Hand('new hand')
    deck = Deck()
    
    deck.shuffle()
    print(find_defining_class(hand, 'shuffle'))
    
    deck.move_cards(hand, 6)
    hand.sort()
    print(hand)

if __name__ == '__main__':
    main()

