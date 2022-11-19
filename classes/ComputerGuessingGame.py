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
        '''
        Set a number for the computer to guess before the game begins
        '''
        set_number = None
        while True:
            set_number = input(f"Please put in a number between {self.difficulty.min_value} and {self.difficulty.max_value}:")

            if re.match("^\d+$", set_number):
                set_number = int(set_number)
                if set_number <= self.difficulty.max_value and set_number >= self.difficulty.min_value:
                    self.number = set_number
                    break
                else:
                    print(f"Please enter a number within the range of {self.difficulty.min_value} and {self.difficulty.max_value}")
            else:
                print("Please enter a valid number")

    _LOWER_REGEX = "^(lower|l)$"
    _HIGHER_REGEX = "^(higher|h)$"

    def next_round(self):
        '''
        Next round of the computer guessing -> Yes the computer could do this all by itself but then it would be no fun!
        '''
        # Guesses number in the middle of the min and max value with a deviation of +/- 20%
        random_number = self.guessed_min + round(((self.guessed_max - self.guessed_min) / 2) * random.uniform(0.8, 1.2))
        print(f"I am guessing: {random_number}? \n")
        answer_correct = yes_no("Is it correct?")

        if not answer_correct and self.number == random_number:
            print("You liar! Someone told me that number is correct! I am not playing with a cheater, back to the menu with you!")
            #TODO: Is there a better solution to this circular import problem? Find one
            from run import main_menu
            main_menu()

        elif answer_correct:
            self.game_end(False)
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
                        print("Lower or higher? Please use a correct value to give me a hint")

                self.rounds_left = self.rounds_left-1

                self.next_round()
            else:
                self.game_end(False)


    def game_end(self, user_won):
        '''
        Shows the game end screen
        '''
        if user_won:
            print("Well you won I have no more guesses left, good job!")
        else:
            print("I won, yay!")

        while True:
            print('''Do you want to play another round or do you want to go back to the menu?\n
1. Play again
2. Back to the menu''')
            user_selection = input("Select: ")
            if re.search("^[1-2]{1}$", user_selection):
                match user_selection:
                    case "1":
                        #TODO: Is there a better solution to this circular import problem? Find one
                        from run import start_game
                        start_game()
                    case "2":
                        #TODO: Is there a better solution to this circular import problem? Find one
                        from run import main_menu
                        main_menu()
            else:
                print("Please select the correct option")

    def start(self):
        '''
        Start the game of the computer guessing
        '''
        self.prepare_game()
        self.next_round()