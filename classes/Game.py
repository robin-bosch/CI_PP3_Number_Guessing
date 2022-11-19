import random
from utils.enums import Guesser
from utils.inputs import yes_no


class Game():
    '''
    Creates game loop
    '''
    def __init__(self, difficulty, guessing):
        self.difficulty = difficulty
        self.rounds_left = difficulty.rounds
        self.guessing = guessing
        self.number = 0
        

    def prepare_game(self):
        '''
        Prepares game
        '''
        if self.guessing == Guesser.COMPUTER:
            self.number = random.randrange(self.difficulty.min, self.difficulty.max)
        else:
            set_number = None
            while True:
                set_number = input(f"Please put in a number between {self.difficulty.min} and {self.difficulty.max}:")

                if set_number >= self.difficulty.min and set_number <= self.difficulty.max:
                    break
                else:
                    print(f"Invalid number: Your number must be between {self.difficulty.min} and {self.difficulty.max}:")
            self.number = set_number

    def next_round(self):
        '''
        Starts the next round
        '''
        if self.guessing == Guesser.COMPUTER:
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
        else:
            input("Guess the number: ")
     

    def start(self):
        '''
        Starts the game with the user guessing
        '''
        self.prepare_game()