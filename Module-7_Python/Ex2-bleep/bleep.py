#!/usr/bin/env python
# vigenere.py encodes a string according to a keystring
# Dani van Enk, 11823526

# used libraries
from sys import argv


def main():
    """
    calls used functions and exits on inccorect parameter count
    """

    if len(argv) != 2:
        exit("Usage: python bleep.py dictionary")
    
    censor(load(argv[1]))


def load(file):
    """
    loads banned words from file

    parameters:
    file - file with banned words

    returns array with banned words
    """

    # open file
    infile = open(file, "r")

    banned_word = []

    # add each word
    for line in infile:
        word = line.strip("\n")
        banned_word.append(word)

    return banned_word


def censor(words):
    """
    censors words froma user_input, the sensored words are given as an array

    parameters:
    words - array with banned words
    """

    # message to be censored
    user_input = input("What message would you like to censor?\n")

    # make an array of words in message
    user_words = user_input.split(" ")

    # setup of counter
    no_of_words = len(user_words)
    word_no = 0

    # loop over each word and checks if word is banned
    for word in user_words:
        # if banned censor else print word
        if word.lower() in words:
            for char in word:
                print("*", end="")
        else:
            print(word, end="")

        # put spaces between words
        if word_no < no_of_words:
            print(" ", end="")

        word_no += 1

    # linebreak
    print()


# executes main
if __name__ == "__main__":
    main()