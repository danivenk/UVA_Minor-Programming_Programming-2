# Implements a cards shuffler and dealer.

class Card:
    """
    Card class defines a card with suit and value
    """
    # initializes a Card object
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return "Card[value = " + self.value + "suit = " + self.suit + "]"

# executes all used functions
def main():
    pass

# run main
if __name__ == "__main__":
    main()
