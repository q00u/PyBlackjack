'''
Deck of cards class
'''
from __future__ import annotations
from typing import *
from card import Card
import random

class Deck(object):
    
    def __init__(self, cards: List[Card]=None):
        '''
        Make a full deck of cards
        or pass in a list of existing cards
        '''
        if cards is None:
            cards=[]
        if len(cards) == 0:
            # make fresh deck
            self.cards: List[Card]=[]
            for suit in range(0,4):
                for rank in range(1,14):
                    self.cards.append(Card(rank,suit))
        else:
            # use passed in cards
            self.cards = cards
    
    def __str__(self):
        return " ".join([str(x) for x in self.cards])
    
    def length(self) -> int:
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self) -> Card:
        return self.cards.pop()

if __name__ == "__main__":
    test = Deck()
    print(test)
    print("  shuffling...")
    test.shuffle()
    print(test)
    print("  draw five...")
    for i in range(0,5):
        print(test.draw())
    print(test)
