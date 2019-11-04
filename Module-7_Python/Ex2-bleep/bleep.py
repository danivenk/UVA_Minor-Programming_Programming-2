from sys import argv


def main():
    # if len(argv) != 2:
    #     exit("Usage: python bleep.py dictionary")
    
    censor(load("D:/danivenk/Dropbox/MProg_Programming/UVA_Minor-Programming_Programming-2/Module-7_Python/Ex2-bleep/banned.txt"))# argv[1]))

def load(file):
    infile = open(file,"r")
    banned_word = []

    for line in infile:
        word = line.strip("\n")
        banned_word.append(word)

    return banned_word

def censor(words):
    user_input = input("What message would you like to censor?\n")

    user_words = user_input.split(" ")

    no_of_words = len(user_words)
    word_no = 0

    for word in user_words:
        if word.lower() in words:
            for char in word:
                print("*", end="")
        else:
            print(word, end="")

        if word_no < no_of_words:
            print(" ", end="")

        word_no += 1

    print()


if __name__ == "__main__":
    main()
