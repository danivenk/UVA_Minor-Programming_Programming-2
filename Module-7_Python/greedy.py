#!/usr/bin/env python
# greedy.py finds the minimum amount of coins needed for the change owed
# Dani van Enk, 11823526


def main():
    """
    finds the minimum amount of coins needed for the change owed
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
    """
    calculates the number of coins owed

    parameters:
    change - the changed owed
    """
    # used variables
    values = [.25, .10, .05, .01]
    coins = 0

    # check how many coins are needed
    for coin in values:
        while True:
            if change - coin >= 0:
                change -= coin
                coins += 1
            else:
                break
    
    # print the number of coins
    print(coins)

# run main
if __name__ == "__main__":
    main()
