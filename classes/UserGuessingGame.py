
from classes.Game import Game
from utils.enums import Guesser


class UserGuessingGame(Game):
    '''
    Create game with the computer guessing
    '''
    def __init__(self, difficulty):
        super().__init__(difficulty, Guesser.USER)

    def prepare_game(self):
        set_number = None
        while True:
            set_number = input(f"Please put in a number between {self.difficulty.min} and {self.difficulty.max}:")

            if set_number >= self.difficulty.min and set_number <= self.difficulty.max:
                break
            else:
                print(f"Invalid number: Your number must be between {self.difficulty.min} and {self.difficulty.max}:")
            self.number = set_number