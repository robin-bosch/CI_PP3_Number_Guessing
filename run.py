import json
import random
import re
import os

from classes.ComputerGuessingGame import ComputerGuessingGame
from classes.Difficulty import Difficulty
from classes.UserGuessingGame import UserGuessingGame
from utils.inputs import take_text_input, yes_no
import utils.worksheet as worksheet
import utils.menus as menus


_DIFFICULTIES = [
    Difficulty("easy", 5, 0, 15),
    Difficulty("medium", 3, 0, 15),
    Difficulty("hard", 5, 0, 50),
    Difficulty("extrme", 5, 0, 100)]

USERNAME_REGEX = "^[a-zA-Z0-9]{3,100}$"
EMAIL_REGEX = "^\S+@\S+\.\S+$"


# Code used: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear_console():
    '''
    Clears console
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    '''
    Prints the welcome logo
    '''
    print('''    _   __                __                 ______                     _            
   / | / /_  ______ ___  / /_  ___  _____   / ____/_  _____  __________(_)___  ____ _
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/
 / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  |__  ) / / / / /_/ / 
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\__,_/\___/____/____/_/_/ /_/\__, /  
                                                                            /____/   ''')


def main():
    '''
    Main
    '''
    menus.main_menu()


if __name__ == "__main__":
    main()
