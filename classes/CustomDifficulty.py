from classes.Difficulty import Difficulty


class CustomDifficulty(Difficulty):
    '''
    Creates a difficulty
    '''
    def __init__(self, row, name, rounds, min_value, max_value):
        super().__init__(name, rounds, min_value, max_value)
        self.row = row
