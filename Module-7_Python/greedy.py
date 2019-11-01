#!/usr/bin/env python
# mario.py makes a mario piramid of a userdefined height
# Dani van Enk, 11823526


def main():
    """
    
    """
    coins_back(get_input("Change owed: "))
    

def get_input(user_promt):
    """
    gets a user input and only accepts positive floating points,
    if input is negative or non numeric it'll promt the user again

    returns the value as an int
    """
    # promt user untill correct format
    while True:
        # promt user
        user_input = input(user_promt)

        # try if user_input is an floating point
        try:
            value = float(user_input)
        except ValueError:
            value = -110

        # if value is positive break
        if value > 0:
            break

    return value

def coins_back(change):
    values = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
    coins = 0

    for coin in values:
        while True:
            if change - coin >= 0:
                change -= coin
                coins += 1
            else:
                break
    
    print(coins)

# run main
if __name__ == "__main__":
    main()
