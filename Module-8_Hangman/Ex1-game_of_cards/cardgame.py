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
        self.value = value
        self.suit = suit

    # string to print when class is printed
    def __str__(self):
        return self.value + "of" + self.suit

    # gets Card value
    def getValue(self):
        return self.value

    # gets Card Suit
    def getSuit(self):
        return self.suit


def main():
    """
    runs used functions
    """
    getCardDeck()


def getCardDeck():
    """
    creates a deck of 52 cards
    """
    # value/suit list and predeclaration of the deck
    values = ["Two", "Three", "Four", "Five", "Six", "Seven",
              "Eight", "Nine", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []

    for value in values:
        for suit in suits:
            deck.append(Card(value, suit))

    for card in deck:
        print(card)


# run main
if __name__ == "__main__":
    main()
