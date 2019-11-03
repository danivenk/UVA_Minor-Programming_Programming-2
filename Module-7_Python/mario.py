#!/usr/bin/env python
# mario.py makes a mario piramid of a userdefined height
# Dani van Enk, 11823526


def main():
    """
    draws a mario  double piramid with a userdefined height
    """
    double_pyramid(get_input("Height: "))

def get_input(user_promt):
    """
    gets a user input and only accepts positive integers,
    if input is negative or non numeric it'll promt the user again

    returns the value as an int
    """
    # promt user untill correct format
    while True:
        # promt user
        user_input = input(user_promt)

        # try if user_input is an integer
        try:
            value = int(user_input)
        except ValueError:
            value = -110

        # if value is positive break
        if 0 <= value < 24:
            break

    return value

def double_pyramid(height):
    """
    draws a mario double piramid of height height

    Parameters:
    height - height of the double piramid
    """
    # loop for every line
    for i in range(height):
        # print left piramid part
        for j in range(height):
            if height - j - 1 <= i:
                print("#", end="")
            else:
                print(" ", end="")

        # print gap
        print("  ", end="")

        # print right piramid part
        for k in range(height):
            if k <= i:
                print("#", end="")

        # print a linebreak
        print()

# run main
if __name__ == "__main__":
    main()