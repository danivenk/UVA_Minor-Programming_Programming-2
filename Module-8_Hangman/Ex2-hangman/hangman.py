import os

PATH = os.path.dirname(os.path.abspath(__file__))


class Lexicon:
	def __init__(self):
		self.words = []

		dictionary = open(PATH + "/dictionary.txt", "r")

		for line in dictionary:
			word = line.strip("\n")
			self.words.append(word)

		dictionary.close()

	def get_words(self, length):
		getting_words = []
		for word in self.words:
			if len(word) == length:
				getting_words.append(word)

		return getting_words

class Hangman:
	def __init__(self, length, num_guesses):
		if length < 1:
			raise Exception("Hangman word needs to have positive length.")
		if num_guesses < 1:
			raise Exception("You need at least one guess to play Hangman.")

		self.length = length
		self.num_guesses = num_guesses
		self.guesses = 0
		self.lex = Lexicon()
		self.words = self.lex.get_words(length)
		self.guess_string = ""
		self.guessed_letters = ""

		for i in range(length):
			self.guess_string += "_"

	def guess(self, letter):
		# Update the game for a guess of letter. Return True if the letter
		# is added to the pattern, return False if it is not.
		letter = letter.lower()

		if len(letter) != 1:
			raise Exception("Please enter one letter at the time")
		if not letter.isalpha():
			raise Exception("Please only enter alphabetical characters")
		if letter not in self.guessed_letters:
			raise Exception("Already guessed that letter")

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
		if self.guesses >= self.num_guesses or self.guesses == 26:
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
		class_str = "letters guessed are " + self.guessed_letters + ", "+ str(len(self.words)) +" words remaining, game "
		if self.won():
			class_str += "won"
		else:
			class_str += "not won"

		return class_str

def main():
	game = Hangman(4, 4)
	guessing = ["x", "y", "z"]
	for letter in guessing:
		game.guess(letter)
		print(game.pattern())
	# print(str(len(game.words)) + ", " + str(game.words))

if __name__ == "__main__":
	main()
