'''
Blackjack game!
'''
from __future__ import annotations
from typing import *
from card import Card
from hand import Hand
from deck import Deck


def getwager(bank: int, lastbet: int = 10) -> int:
    valid: bool = False
    while not valid:
        # update display
        print(f"Bank: {bank}")
        wag = input(f"How much would you like to bet? [{lastbet}]: ")
        if len(wag) == 0:
            wag = str(lastbet)
        try:
            iwag = int(wag)
        except ValueError as ex:
            print("Was that an integer?")
        except TypeError as ex:
            print("What was that?!")
        else:
            if iwag < 1:
                print("Try to be more positive")
            elif iwag > bank:
                print("You don't have that much!")
            else:
                valid = True
    return iwag


def getplay() -> bool:
    while True:
        play = input("Hit or Stand? [h/S]: ").lower()
        if play == "" or play == "s":
            return False
        elif play == "h":
            return True
        else:
            print("Not sure I understood that...")


# Main
print("Welcome to Blackjack!")
playing: bool = True
while playing:
    bank: int = 100
    lastbet: int = 10
    deck: Deck = Deck([])
    game: bool = True
    while game:
        if bank == 0:
            print("BANKRUPT!")
            game = False
        else:
            if deck.length() < 52/2:
                deck = Deck()
                deck.shuffle()
                print("..shuffling..")
            # bet
            lastbet = getwager(bank, lastbet)
            bank -= lastbet
            print(f"Bet: {lastbet}, Bank: {bank}")
            # hand
            dealer = Hand()
            player = Hand()
            # deal
            dealer.add(deck.draw())
            player.add(deck.draw())
            dealer.add(deck.draw())
            player.add(deck.draw())
            # redraw
            print(
                f"Dealer: {dealer.dealershow()}, total: {range(dealer.dealersum(),dealer.dealersum()+11)}")
            print(f"Player: {player}, total: {player.sum()}")
            # Dealer blackjack?
            if dealer.sum() == 21 and player.sum() < 21:
                print("Dealer blackjack!")
                print(f"Lost {lastbet}")
                continue
            # Player blackjack?
            if player.sum() == 21:
                print(f"BLACKJACK! Won {int(lastbet*1.5)}")
                bank += int(lastbet + lastbet*1.5)
                continue
            # Player's turn
            while getplay():
                player.add(deck.draw())
                print(f"Dealt {player.hand[-1]}, total: {player.sum()}")
                if player.sum() > 21:
                    break
            if player.sum() > 21:
                print(f"BUST! Lost {lastbet}")
                continue
            # Dealer's turn
            print(f"Dealer: {dealer}, total: {dealer.sum()}")
            while dealer.sum() < player.sum() and dealer.sum() < 21:
                dealer.add(deck.draw())
                print(f"Dealt {dealer.hand[-1]}, total: {dealer.sum()}")
            if dealer.sum() > 21:
                print(f"Dealer busts! Won {lastbet}")
                bank += lastbet*2
            elif dealer.sum() == player.sum():
                print("Push...")
                bank += lastbet
            elif dealer.sum() > player.sum():
                print(f"Dealer wins. Lost {lastbet}")
            else:
                print("How did I get here?!?")
    # Play again?
    playing = False
