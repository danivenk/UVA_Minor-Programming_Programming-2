# mario.py makes a mario piramid of a userdefined height


def main():
    """
    draws a mario  double piramid with a userdefined height
    """
    double_pyramid(get_input())

def get_input():
    """
    gets a user input and only accepts positive integers,
    if input is negative or non numeric it'll promt the user again

    returns the value as an int
    """
    # promt user untill correct format
    while True:
        # promt user
        height = input("Height ")

        # try if height is an integer
        try:
            height = int(height)
        except ValueError:
            height = -110

        # if height is positive break
        if height > 0:
            break

        return height

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
            else:
                print(" ", end="")
        
        # print a linebreak
        print()

# run main
if __name__ == "__main__":
    main()
