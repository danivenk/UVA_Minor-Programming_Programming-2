from sys import argv


def main():
    censor(load(argv[1]))

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

    for word in user_words:
        if word in words:
            for char in word:
                print("*", end="")
        else:
            print(word, end="")
        print(" ", end="")


if __name__ == "__main__":
    main()
