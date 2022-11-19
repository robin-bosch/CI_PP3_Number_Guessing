
import random
import re
from classes.Game import Game
from utils.enums import Guesser


class UserGuessingGame(Game):
    '''
    Create game with the computer guessing
    '''
    def __init__(self, difficulty):
        super().__init__(difficulty, Guesser.USER)

    def next_round(self):
        if self.rounds_left > 0:
            while True:
                guessed_number = input("Guess the number:\n")

                # Check
                if re.match("^\d+$", guessed_number):
                    guessed_number = int(guessed_number)
                    if guessed_number <= self.difficulty.max_value and guessed_number >= self.difficulty.min_value:
                        self.rounds_left = self.rounds_left-1
                        if guessed_number == self.number:
                            print("You won")
                            #TODO: Add winning screen
                        elif guessed_number < self.number:
                            print("Not the number I picked!\nThe number is lower")
                            self.next_round()
                        else:
                            print("Not the number I picked!\nThe number is higher")
                            self.next_round()

                    else:
                        print(f"Please enter a number within the range of {self.difficulty.min_value} and {self.difficulty.max_value}")
                else:
                    print("Please enter a valid number")
        else:
            print(f"No more rounds left, you didn't get the number.\n I picked {self.number} as my random number")

    
    def prepare_game(self):
        self.number = random.randrange(self.difficulty.min_value, self.difficulty.max_value)

