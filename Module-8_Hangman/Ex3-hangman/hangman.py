#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
hangman.py creates a game of hangman
Dani van Enk, 11823526
"""

# import library
import os

# path to directory where this file is located
PATH = os.path.dirname(os.path.abspath(__file__))

# number of letters in the alphabet
ALPHA = 26


class Lexicon:
	"""
	the Lexicon class defines a word list with word from the dictionary

	methods:
	get_words() - gets a list of all words of a certain length in the dictionary
	"""

	def __init__(self):
		"""
		initializes the wordlist from the dictionary file
		"""

		self.words = []

		# append each word in the dictionary file to the word list
		with open(PATH + "/dictionary.txt", "r") as file:
			for line in file:
				word = line.strip("\n")
				self.words.append(word)

	def get_words(self, length):
		"""
		gets a word list with words of length from the dictionary

		parameters:
		length - length of the words in the returned word list

		returns a word list
		"""

		getting_words = []

		# checking for withs with of len length and appending them to the list
		for word in self.words:
			if len(word) == length:
				getting_words.append(word)

		# assume getting_words is not empty
		assert len(getting_words) > 0

		return getting_words

class Hangman:
	"""
	defines a hangman game

	methods:
	guess()				- guesses a letter;
	pattern()			- returns the current play pattern;
	guess_string()		- returns guessed letters;
	consistent_word()	- returns a word consistent with current play pattern;
	finished()			- checks if the game is finished;
	won()				- checks if the game is won;
	lost()				- checks if the game is lost
	"""

	def __init__(self, length, num_guesses):
		"""
		initializes a game of hangman

		gives an error if length not positive or number of guesses not positive

		parameters:
		length		- length of the hangman word
		num_guesses	- maximum number of guesses
		"""

		# assume length not 0 and there are more than 0 guesses
		assert length > 0 and num_guesses > 0

		self.length = length
		self.num_guesses = num_guesses
		self.guesses = 0
		self.lex = Lexicon()
		self.words = self.lex.get_words(length)
		self.guess_string = ""
		self.guessed_letters = ""
		self.guess_string = length * "_"

	def guess(self, letter):
		# Update the game for a guess of letter. Return True if the letter
		# is added to the pattern, return False if it is not.
		letter = str(letter).lower()

		assert letter.isalpha() and len(letter) == 1 and letter not in self.guessed_letters

		possible_combinations = []
		self.guesses += 1

		self.guessed_letters += letter

		for word in self.words:
			letter_pos_string = ""
			for char in range(len(word)):
				if word[char] != self.guess_string[char] and word[char] == letter:
					letter_pos_string += letter
				else:
					letter_pos_string += self.guess_string[char]

			word_added = False

			if len(possible_combinations) == 0:
				possible_combinations.append([letter_pos_string, 1, [word]])
			else:
				for item in possible_combinations:
					if letter_pos_string in item:
						item[1] += 1
						item[2].append(word)
						word_added = True
						break

				if not word_added:
					possible_combinations.append([letter_pos_string, 1, [word]])

		dummy = 0

		for item in possible_combinations:
			if len(item[2]) > dummy:
				dummy = len(item[2])
				self.words = item[2]
				self.guess_string = item[0]

		if letter in self.guess_string:
			return True
		else:
			return False


	def pattern(self):
		# Return a string of the current game pattern. Use underscores in
		# place of missing letters. Example: "_AN_MAN".
		return self.guess_string

	def guessed_string(self):
		# Produce a string of all letters guessed so far, in the order they
		# were guessed.
		return self.guessed_letters

	def consistent_word(self):
		# Produce a word that is consistent with the current pattern.
		return self.words[0]

	def finished(self):
		# Return True if the game is finished, otherwise False.
		if self.guesses >= self.num_guesses or self.guesses == ALPHA:
			return True
		else:
			return False

	def won(self):
		# Return True if the game is finished and the player has won,
		# otherwise False.
		if self.finished() and "_" not in self.guess_string:
			return True
		else:
			return False

	def lost(self):
		# Return True if the game is finished and the player has lost,
		# otherwise False.
		if self.finished() and "_" in self.guess_string:
			return True
		else:
			return False

	def __str__(self):
		# Return a string representation of the game with some relevant
		# statistics.
		class_str = f"letters guessed are {self.guessed_letters}, \
					{len(self.words)} words remaining, guesses remaining \
					{self.num_guesses - self.guesses}"

		return class_str

def main():
	user_length = get_number("With what length of a word would you like to play? ")
	
	user_guesses = get_number("How many guesses would you like? ")
	while 1:
		user_statistics = input("Would you like to see statistics of the game while playing? (y/n) ")
		if user_statistics[0].lower() == "y":
			user_stat = True
			break
		elif user_statistics[0].lower() == "n":
			user_stat = False
			break
	
	game_play(user_length, user_guesses, user_stat)

def get_number(text):
	number = input(text)

	try:
		integer = int(number)
	except ValueError:
		get_number(text)

	return integer

def game_play(length, num_guesses, statistics):

	game = Hangman(length, num_guesses)

	print("WELCOME TO EVIL HANGMAN >=)")
	print(f"I have a word in mind of {length} letters")

	while not game.finished():
		letter = input("Guess a letter: ")
		if game.guess(letter):
			print(f"The letter {letter} is in the word :(")
		else:
			print(f"The letter {letter} is not in the word >=)")
		print(game.pattern())

		if statistics:
			print(game)
		

if __name__ == "__main__":
	main()
