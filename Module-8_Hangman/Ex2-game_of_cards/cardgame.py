#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
cardgame.py creates a deck of cards shuffles it and deals 4 cards
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
        
        self.value = value
        self.suit = suit

    def description(self):
        """
        return description of the Card class

        returns readable string
        """

        return f"{self.value} of {self.suit}"

    def getValue(self):
        """
        gets value of the Card

        returns Card value
        """
        
        return self.value

    def getSuit(self):
        """
        gets suit of the Card

        returns Card suit
        """

        return self.suit


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

        self._values = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                        '10', 'J', 'Q', 'K']
        self._suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self._cards = []

        for suit in self._suits:
            for value in self._values:
                self._cards.append(Card(value, suit))

    def description(self):
        """
        return description of the Deck class

        returns readable string
        """

        return f"There are {len(self._cards)} cards in the deck"

    def shuffle(self):
        """
        shuffles the deck of cards
        """

        random.shuffle(self._cards)

    def deal(self):
        """
        deals a card and removes it from the deck

        returns a card
        """
        assert len(self._cards) > 0
        return self._cards.pop()


def main():
    """
    runs used functions
    """

    # create a deck
    deck = Deck()
    
    for i in range(4):
        dealRandomCard(deck)


def dealRandomCard(deck):
    """
    deals a random card from a deck of cards
    """

    # print current state of the deck
    print(deck.description())

    # shuffles the deck
    deck.shuffle()

    # deal a card
    print(f"you've drawn the: {deck.deal().description()}")


# run main
if __name__ == "__main__":
    main()
