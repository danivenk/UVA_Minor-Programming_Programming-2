#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
hangman.py creates a game of evil hangman
Dani van Enk, 11823526
"""


# import library
import os
import cs50


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
	defines a evil hangman game

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
		initializes a game of evil hangman with words of len length and
			with maximum number of guesses of num_guesses

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
		"""
		guesses a letter and eliminates the words from which it is easy
			to guess the word for the user and adds the letter corrispondingly

		give an error if letter isn't an alpha, more than 1 letter or
			already guessed

		parameters:
		letter - letter to be guessed

		returns whether or not the letter has been added to the pattern
		"""
		
		# make sure letter is a string
		letter = str(letter).lower()

		# assume letter is 1 character, a letter and not yet guessed
		assert letter.isalpha() and len(letter) == 1 and \
			letter not in self.guessed_letters

		possible_combinations = []
		self.guesses += 1

		# add letter to guessed_letter
		self.guessed_letters += letter

		# loop over each word 
		for word in self.words:
			letter_pos_string = ""

			# loop over each letter
			for char in range(len(word)):

				# add letter to position if letter not in guess_string for letter
				if word[char] != self.guess_string[char] and word[char] == letter:
					letter_pos_string += letter

				# else add guess_string letter
				else:
					letter_pos_string += self.guess_string[char]

			# set bool for if word is added
			word_added = False

			# initialize possible_combinations in correct format if not yet
			#	initialized else add combination to possible combinations
			if len(possible_combinations) == 0:
				possible_combinations.append([letter_pos_string, 1, [word]])
			else:

				# loop over each item in possible combinations
				for item in possible_combinations:

					# count words for each possible combinations and save words
					if letter_pos_string in item:
						item[1] += 1
						item[2].append(word)
						word_added = True
						break

				# if combination is not yet in possible_combinations add it
				if not word_added:
					possible_combinations.append([letter_pos_string, 1, [word]])

		# dummy counter
		dummy = 0

		# find the possible combination with the most words associated
		for item in possible_combinations:
			# if found combination with more words
			if len(item[2]) > dummy:
				dummy = len(item[2])
				self.words = item[2]
				self.guess_string = item[0]

		# return true if letter is added else false
		if letter in self.guess_string:
			return True
		else:
			return False


	def pattern(self):
		"""
		returns current guess_string
		"""

		return self.guess_string

	def guessed_string(self):
		"""
		returns all guessed letters in order of guessed
		"""

		return self.guessed_letters

	def consistent_word(self):
		"""
		returns a word consistent with current pattern
		"""
		
		return self.words[0]

	def finished(self):
		"""
		check if game is finished

		returns true if game if finished else false
		"""
		
		# when guessed more than maximum number of guesses or
		# 	if all letters are guessed return true else false
		if self.guesses >= self.num_guesses or self.guesses == ALPHA:
			return True
		else:
			return False

	def won(self):
		"""
		checks if game is won

		returns true if won else false
		"""
		
		# if game finished and no _ left return true else false
		if self.finished() and "_" not in self.guess_string:
			return True
		else:
			return False

	def lost(self):
		"""
		checks if game is lost

		returns true if lost else false
		"""
		
		# if game finished and _ left return true else false
		if self.finished() and "_" in self.guess_string:
			return True
		else:
			return False

	def __str__(self):
		"""
		returns statistics of game
		"""
		
		# statistics of the game, guessed_letters, number of words left
		#	and guesses left
		class_str = f"letters guessed are {self.guessed_letters}, " + \
					f"{len(self.words)} words remaining, guesses remaining" + \
					f"{self.num_guesses - self.guesses}"

		return class_str


def main():
	"""
	promts user for word length, max number of guesses and
		if user wants statistics to be shown and
		plays a game of evil hangman with those parameters
	"""

	# promts user for word length
	user_length = cs50.get_int("With what length of a word" + \
								" would you like to play? ")
	
	# promts user for max number of guessess
	user_guesses = cs50.get_int("How many guesses would you like? ")

	# promts user for statistic and converts it to a bool
	while 1:
		user_statistics = input("Would you like to see statistics" + \
								" of the game while playing? (y/n) ")
		if user_statistics[0].lower() == "y":
			user_stat = True
			break
		elif user_statistics[0].lower() == "n":
			user_stat = False
			break
	
	# plays a game of hangman
	game_play(user_length, user_guesses, user_stat)


def game_play(length, num_guesses, statistics):
	"""
	plays a game of evil 
	
	parameters:
	length		- length of the word to be guessed
	num_guesses	- maximum number of guesses
	statistics	- bool if statistics it to be shown
	"""

	# create evil hangman object
	game = Hangman(length, num_guesses)

	# greeting
	print("WELCOME TO EVIL HANGMAN >=)")
	print(f"I have a word in mind of {length} letters")

	# evil hangman rounds untill finished
	while not game.finished():

		# guess letter
		letter = input("Guess a letter: ")
		if game.guess(letter):
			print(f"The letter {letter} is in the word :(")
		else:
			print(f"The letter {letter} is not in the word >=)")

		# print pattern
		print(game.pattern())

		# print statistics
		if statistics:
			print(game)
		

# run main
if __name__ == "__main__":
	main()
