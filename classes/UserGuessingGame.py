
import random
import re

# Custom imports
import run
import classes.User as user
from classes.Game import Game
from utils.enums import Guesser
import utils.menus as menus


class UserGuessingGame(Game):
    '''
    Create game with the computer guessing
    '''
    def __init__(self, difficulty):
        super().__init__(difficulty, Guesser.USER)

    def next_round(self):
        '''
        Play one round of the game
        '''
        print(f"Rounds left: {self.rounds_left}")
        self.rounds_left = self.rounds_left-1
        while True:
            guessed_number = input(f"Guess the number between \
{self.difficulty.min_value} and {self.difficulty.max_value}\n")

            # Check for a digit
            if re.match(r"^\d+$", guessed_number):
                guessed_number = int(guessed_number)

                # Check if the guessed number in the range
                if guessed_number <= self.difficulty.max_value and \
                   guessed_number >= self.difficulty.min_value:

                    if guessed_number == self.number:
                        self.game_end(True)
                    elif guessed_number < self.number:
                        print("Not the number I picked!")
                        print("The number is higher!")
                        if self.rounds_left > 0:
                            self.next_round()
                        else:
                            self.game_end(False)
                    else:
                        print("Not the number I picked!")
                        print("The number is lower!")
                        if self.rounds_left > 0:
                            self.next_round()
                        else:
                            self.game_end(False)
                else:
                    print(f"Please enter a number within the range of \
{self.difficulty.min_value} and {self.difficulty.max_value}")

            else:
                print("Please enter a valid number")

    def game_end(self, user_won):
        '''
        Shows the game end screen
        '''
        run.clear()
        if user_won:
            print(f"Correct number! You won, {user.get_user().username}!")
        else:
            print(f"No more rounds left, you didn't get the number.\n\
I picked {self.number} as my random number")

        while True:
            print("Do you want to play another round \
or do you want to go back to the menu?\n \
1. Play again\n\
2. Back to the menu\n")
            user_selection = input("Select: ")
            if re.search("^[1-2]{1}$", user_selection):
                match user_selection:
                    case "1":
                        menus.start_game()
                    case "2":
                        menus.main_menu()
            else:
                print("Please select the correct option")

    def prepare_game(self):
        '''
        Prepares the game with a random number for the user to guess
        '''
        self.number = random.randrange(
                        self.difficulty.min_value,
                        self.difficulty.max_value)

    def start(self):
        '''
        Start the game of the computer guessing
        '''
        self.prepare_game()
        self.next_round()
