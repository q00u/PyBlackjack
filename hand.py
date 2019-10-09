'''
Hand of cards class
'''
from __future__ import annotations
from typing import *
from card import Card

class Hand(object):    
    def __init__(self, cards:List[Card]=None):
        '''
        Make an empty hand of cards
        or pass in a list existing cards
        '''
        if cards is None:
            cards=[]
        # for x in cards:
        #     if (type(x) is not Card):
        #         raise TypeError("Hand can only hold Card types")
        self.hand = cards
    
    def add(self, card: Card):
        # if (type(card) is not Card):
        #     raise TypeError("Can only add Cards to hand")
        self.hand.append(card)
        
    def dealershow(self) -> str:
        if len(self.hand) != 2:
            raise Exception("Dealer should be holding two cards at this time...")
        return str(self.hand[0])+" 🂠"
        
    def __str__(self):
        return " ".join([str(x) for x in self.hand])
    
    def sum(self) -> int:
        return sum([x.value() for x in self.hand])
    
    def dealersum(self) -> int:
        if len(self.hand) != 2:
            raise Exception("Dealer should be holding two cards at this time...")
        return self.hand[0].value()


if __name__ == "__main__":
    #Test hand.py
    test = Hand()
    test.add(Card(1,0))
    test.add(Card(5,2))
    print(test)
    print(f"Total: {test.sum()}")
    test2 = Hand([Card(1,2), Card(1,3), Card(7,1)])
    print(test2)
    print(f"Total: {test2.sum()}")