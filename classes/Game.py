class Game():
    '''
    Abstract class for games, do not initialize
    '''
    def __init__(self, difficulty, guessing):
        self.difficulty = difficulty
        self.rounds_left = difficulty.rounds
        self.guessing = guessing
        self.number = 0
