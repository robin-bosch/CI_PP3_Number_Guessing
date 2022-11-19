import random
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

    def next_round(self):
        #TODO Replace with proper number
        print("I am guessing: 5?\n ")
        answer_correct = yes_no("Is it correct? Y/N")

        if answer_correct:
            print("I won")
        else:
            if self.rounds_left > 0:
                self.rounds_left = self.rounds_left-1

                print("Next round: ")
                self.next_round()
            else:
                print("You lost")

    def start(self):
        '''
        Start the game of the computer guessing
        '''
        self.prepare_game()