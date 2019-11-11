#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
cardgame.py creates a deck of cards shuffles it and deals a card
Dani van Enk, 11823526
"""

# import library
import random

class Card:
    """
    Card class defines a card with suit and value
    
    methods:
    description() - returns description of the Card class;
    getValue() - gets Card value;
    getSuit() - gets Card suit
    """
    def __init__(self, value, suit):
        """
        initializes the Card class

        parameters:
        value - value of the card as a string;
        suit - suit of the card as a string
        """
        self._value = value
        self._suit = suit

    def description(self):
        """
        return description of the Card class

        returns readable string
        """
        return f"{self._value} of {self._suit}"

    def getValue(self):
        """
        gets value of the Card

        returns Card value
        """
        return self._value

    def getSuit(self):
        """
        gets suit of the Card

        returns Card suit
        """
        return self._suit


class Deck:
    """
    defines a deck of 52 cards
    
    methods:
    description() - returns description of the Deck class;
    shuffle() - shuffel the deck of cards;
    deal() - pick one random card from the deck
    """
    def __init__(self):
        """
        initializes the Deck class
        """
        self._values = ["Two", "Three", "Four", "Five", "Six", "Seven", \
                        "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        self._suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = []

        for suit in self._suits:
            for value in self._values:
                self.cards.append(Card(value, suit))

    def description(self):
        """
        return description of the Deck class

        returns readable string
        """
        return f"There are {len(self.cards)} cards in the deck"

    def shuffle(self):
        """
        shuffles the deck of cards
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        deals a card and removes it from the deck

        returns a card
        """
        return self.cards.pop(0)


def main():
    """
    runs used functions
    """
    dealRandomCard()

def dealRandomCard():
    """
    deals a random card from a deck of 52 cards
    """
    # create a deck
    deck = Deck()

    # print current state of the deck
    print(deck.description())

    # shuffles the deck
    deck.shuffle()
    
    # deal a card
    print(deck.deal())

    # print current state of the deck
    print(deck.description())


# run main
if __name__ == "__main__":
    main()
