import random
from utils.enums import Guesser
from utils.inputs import yes_no


class Game():
    '''
    Abstract class for games, do not initialize
    '''
    def __init__(self, difficulty, guessing):
        self.difficulty = difficulty
        self.rounds_left = difficulty.rounds
        self.guessing = guessing
        self.number = 0