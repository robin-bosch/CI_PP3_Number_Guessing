import os

# Custom imports
from classes.Difficulty import Difficulty
import utils.menus as menus


_DIFFICULTIES = [
    Difficulty("easy", 5, 0, 15),
    Difficulty("medium", 3, 0, 15),
    Difficulty("hard", 5, 0, 50),
    Difficulty("extreme", 5, 0, 100)]


# Code used:
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear():
    '''
    Clears console
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    '''
    Prints the welcome logo
    '''
    print(r'''
    _   __                   ______
   / | / /_  ______ ___     / ____/_  _____  __________
  /  |/ / / / / __ `__ \   / / __/ / / / _ \/ ___/ ___/
 / /|  / /_/ / / / / / /  / /_/ / /_/ /  __(__  |__  )
/_/ |_/\__,_/_/ /_/ /_/   \____/\__,_/\___/____/____/
''')


def main():
    '''
    Run main menu
    '''
    menus.main_menu()


if __name__ == "__main__":
    main()
