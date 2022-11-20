import json
import random
import re
import os

from classes.Difficulty import Difficulty

import utils.menus as menus


_DIFFICULTIES = [
    Difficulty("easy", 5, 0, 15),
    Difficulty("medium", 3, 0, 15),
    Difficulty("hard", 5, 0, 50),
    Difficulty("extreme", 5, 0, 100)]


# Code used:
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear_console():
    '''
    Clears console
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    '''
    Prints the welcome logo
    '''
    # Can't fix the line length error, as it would break the logo
    print(r'''    _   __                __                 ______                     _
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
