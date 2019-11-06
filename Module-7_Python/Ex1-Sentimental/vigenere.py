#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
vigenere.py encodes a string according to a keystring
Dani van Enk, 11823526
"""

# import library
import sys


def main():
    """
    executes the encode function
    """
    key, plain = get_key_plain()
    encode(key, plain)


def get_key_plain():
    """
    gets the command line parameters (only accepting 1)
    and asks user for a text to cipher

    returns the key from the commandline and the plain text
    """
    if len(sys.argv) != 2:
        exit("Usage: python vigenere.py k")

    # get plaintext
    user_input = input("plaintext: ")
    
    return sys.argv[1], user_input


def char_to_number(char):
    """
    gets the number of a given character A/a => 0, B/b => 1 etc.

    parameters:
    char - character to get the number of

    returns the number
    """
    if not char.isalpha():
        return
    elif char.isupper():
        return (ord(char) - ord("A"))
    else:
        return (ord(char) - ord("a"))


def encode(key, plain):
    """
    encodes the plaintext given by the user using the key
    only alphabetical characters get ciphered

    parameter:
    key - a string to use to cipher the text with
    plain - a string to cipher
    """
    print("ciphertext: ", end="")

    # used variables
    pos = 0
    key_len = len(key)

    # loop over every character in the text
    for char in plain:
        key_pos = pos % key_len
        # leave non-alphabetical characters alone
        if not char.isalpha():
            print(char, end="")
        # cipher characters
        elif char.isupper():
            cipher = chr((char_to_number(char) + char_to_number(key[key_pos])) \
                % 26 + ord("A"))
            
            print(cipher, end="")
            pos += 1
        else:
            cipher = chr((char_to_number(char) + char_to_number(key[key_pos])) \
                        % 26 + ord("a"))
            
            print(cipher, end="")
            pos += 1

    print()


# run main
if __name__ == "__main__":
    main()
