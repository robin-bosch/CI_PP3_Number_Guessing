class Difficulty():
    '''
    Creates a difficulty
    '''

    def __init__(self, name, rounds, min_value, max_value):
        self.name = name

        if not isinstance(min_value, int):
            raise ValueError("Minimal value must be an integer.")
        self.min_value = min_value

        if not isinstance(max_value, int):
            raise ValueError("Maximal value must be an integer.")
        self.max_value = max_value

        if not isinstance(rounds, int):
            raise ValueError("Rounds must be an integer.")
        self.rounds = rounds
