"""
Program: numberguessGUI.py
Author: Susan 11/15/2021

GUI based version of the number guessing game from previous chapters.
***NOTE: the file breezypythongui.py must be in the same directory as this file for the application to work.***
"""

import random
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
	"""Plays a number guessing game with the user."""

	def __init__(self):
		"""Sets up the window, widgets, and data."""
		EasyFrame.__init__(self, title = "Guessing Game", width = 360, height = 180)
		# Initialize the instance variables for the data
		self.myNumber = random.randint(1, 100)
		self.count = 0
		
		# Create and add widgets to the window
		greeting = "Guess a number between 1 and 100???"
		self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0, sticky = "NSEW", columnspan = 2)
		self.addLabel(text = "Your guess:", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.nextButton = self.addButton(text = "Submit", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)
		self.newButton["background"] = "yellow"
		self.guessField["background"] = "pink"

	def nextGuess(self):
		"""Processes the user's next guess."""
		self.count += 1
		guess = self.guessField.getNumber()
		# decide the outcome of the game
		if guess == self.myNumber:
			self.hintLabel["text"] = "You guessed it in " + str(self.count) + " attempt(s)!"
			self.nextButton["state"] = "disabled"
		elif guess < self.myNumber:
			self.hintLabel["text"] = "Sorry, too low!"
		else:
			self.hintLabel["text"] = "Sorry, too high!"

	def newGame(self):
		"""Resets the data and GUI to their original states."""
		self.myNumber = random.randint(1, 100)
		self.count = 0 
		self.hintLabel["text"] = "Guess a number between 1 and 100???"
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"

# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	GuessingGame().mainloop()

# global call to main()
if __name__ == "__main__":
	main()