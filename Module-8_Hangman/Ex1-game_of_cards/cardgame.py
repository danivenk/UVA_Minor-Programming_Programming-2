# Implements a cards shuffler and dealer.


class Card:
    """
    Card class defines a card with suit and value
    
    methods:
    getValue() - gets Card value
    getSuit() - gets Card suit
    """
    # initializes a Card object

    def __init__(self, value, suit):
        """
        
        """
        self.value = value
        self.suit = suit

    # string to print when class is printed
    def __str__(self):
        return self.value + " of " + self.suit

    # gets Card value
    def getValue(self):
        return self.value

    # gets Card Suit
    def getSuit(self):
        return self.suit


class Deck:
    """
    defines a deck of 52 cards
    
    methods:
    shuffle() - shuffel the deck of cards
    deal() - pick one random card from the deck
    """
    def __init__(self):
        # value/suit list and predeclaration of the deck
        self.values = ["Two", "Three", "Four", "Five", "Six", "Seven", \
                        "Eight", "Nine", "Jack", "Queen", "King", "Ace"]
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.deck = []

        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(value, suit))


def main():
    """
    runs used functions
    """
    pass


# run main
if __name__ == "__main__":
    main()
