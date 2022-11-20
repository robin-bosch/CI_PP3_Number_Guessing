
import random
import re
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
        if self.rounds_left > 0:
            while True:
                guessed_number = input("Guess the number:\n")

                # Check
                if re.match(r"^\d+$", guessed_number):
                    guessed_number = int(guessed_number)
                    if guessed_number <= self.difficulty.max_value and \
                       guessed_number >= self.difficulty.min_value:
                        self.rounds_left = self.rounds_left-1
                        if guessed_number == self.number:
                            self.game_end(True)
                        elif guessed_number < self.number:
                            print("Not the number I picked!")
                            print("The number is higher!")
                            self.next_round()
                        else:
                            print("Not the number I picked!")
                            print("The number is lower!")
                            self.next_round()

                    else:
                        print(f"Please enter a number within the range of \
{self.difficulty.min_value} and {self.difficulty.max_value}")

                else:
                    print("Please enter a valid number")
        else:
            self.game_end(False)

    def game_end(self, user_won):
        '''
        Shows the game end screen
        '''
        if user_won:
            print("Correct number! You won!")
        else:
            print(f"No more rounds left, you didn't get the number.\n \
I picked {self.number} as my random number")

        while True:
            print("Do you want to play another round \
                  or do you want to go back to the menu?\n \
                  1. Play again \
                  2. Back to the menu")
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
