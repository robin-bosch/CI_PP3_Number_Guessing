import random
import re
from classes.Game import Game
from utils.enums import Guesser
from utils.inputs import yes_no


class ComputerGuessingGame(Game):
    '''
    Create game with the computer guessing
    '''
    def __init__(self, difficulty):
        super().__init__(difficulty, Guesser.COMPUTER)
        self.guessed_numbers = []
        self.guessed_max = self.difficulty.max_value
        self.guessed_min = self.difficulty.min_value

    def prepare_game(self):
        self.number = random.randrange(self.difficulty.min_value, self.difficulty.max_value)

    _LOWER_REGEX = "^(lower|l)$"
    _HIGHER_REGEX = "^(higher|h)$"

    def next_round(self):
        # Guesses number in the middle of the min and max value with a deviation of +/- 20%
        random_number = self.guessed_min + round(((self.guessed_max - self.guessed_min) / 2) * random.uniform(0.8, 1.2))
        print(f"I am guessing: {random_number}? \n")
        answer_correct = yes_no("Is it correct? Y/N")

        if not answer_correct and self.number == random_number:
            print("You liar! Someone told me that number is correct! I am not playing with cheater, back to the menu with you!")

        elif answer_correct:
            print("I won")
            # from run import main_menu
            # main_menu()
        else:
            if self.rounds_left > 0:
                while True:
                    hint_value = input("Is it the your number lower or higher?\n")

                    if re.match(ComputerGuessingGame._LOWER_REGEX, hint_value, re.IGNORECASE):
                        self.guessed_max = random_number - 1
                        break
                    elif re.match(ComputerGuessingGame._HIGHER_REGEX, hint_value, re.IGNORECASE):
                        self.guessed_min = random_number + 1
                        break
                    else:
                        print("Lower or higher? Please use a correct value to give a hint to the computer")

                self.rounds_left = self.rounds_left-1

                self.next_round()
            else:
                print("Well you won, good job!")

    def start(self):
        '''
        Start the game of the computer guessing
        '''
        self.prepare_game()
        self.next_round()