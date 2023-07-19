"""
Program: textFieldDemo.py
Author: Jess

Random number guessing program using GUI
"""

from breezypythongui import EasyFrame
import random
# Other imports go here

# Class header
class GuessingGame(EasyFrame):
    # Definition of our class constructor method
    def __init__(self):
        EasyFrame.__init__(self, title= "Guessing Game", width= 260, height= 180)

        # Initialize the instance variables for the class
        self.randomNumber = random.randint(1,10)
        self.count = 0

        # Create and add widgets to the window
        self.hintLabel = self.addLabel(text= "Guess a Number Between 1 and 100", row= 0, column= 0, columnspan= 2, sticky= "NSEW")
        self.addLabel(text= "Your guess:", row= 1, column= 0)
        self.guessField = self.addIntegerField(value= 0, row= 1, column= 1)
        self.nextButton = self.addButton(text= "Next", row= 2, column= 0, command= self.nextGuess)
        self.newButton = self.addButton(text= "New Game", row= 2, column= 1, command= self.newGame)

    # Definition of the nextGuess() function
    def nextGuess(self):
        self.count += 1
        guess = self.guessField.getNumber()
        # Logic that determines the game's outcome 
        if guess == self.randomNumber:
            self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " attempts!"
            self.nextButton["state"] = "disabled"
        elif guess < self.randomNumber:
            self.hintLabel["text"] = "Sorry, your guess was too small"
        else:
            self.hintLabel["text"] = "Sorry, your guess was too large!"

    # Definition of the newGame() function
    def newGame(self):
        """Resets the data and GUI to their original states"""
        self.randomNumber = random.randint(1, 10)
        self.count = 0
        self.hintLabel["text"] = "Guess a Number Between 1 and 100"
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"


# Global definition of the main() method
def main():
    GuessingGame().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()

