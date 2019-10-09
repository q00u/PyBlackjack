'''
Card class
Constants = FACES, VALUE, SUITS
'''
from __future__ import annotations
from typing import *

class Card(object):
    
    FACES = [0,'A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    VALUE = [0,11,2,3,4,5,6,7,8,9,10,10,10,10]
    SUITS = ['♠','♡','♢','♣']
    
    def __init__(self, rank: int, suit: int):
        '''
        rank = range(1..13) Ace ... King
        suit = range(0..3) ['♠','♡','♢','♣']
        '''
        if rank not in range(1,14):
            raise ValueError("rank must be in range 1..14")
        elif suit not in range(0,4):
            raise ValueError("suit must be in range 0..3")
        else:
            self.rank: int=rank
            self.suit: int=suit
    
    def __str__(self):
        return str(self.FACES[self.rank])+str(self.SUITS[self.suit])
    
    def __lt__(self, other: Card):
        return self.rank < other.rank
    
    def value(self) -> int:
        return Card.VALUE[self.rank]
