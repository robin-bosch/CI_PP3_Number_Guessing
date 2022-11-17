from enum import Enum
import random
import re
import os
from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials


class Guesser(Enum):
    '''
    Enum for the guesser
    '''
    COMPUTER = "computer"
    USER = "user"


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('number_guessing')



class Difficulty():
    '''
    Creates a difficulty
    '''
    def __init__(self, rounds, min_value, max_value):
        self.rounds = rounds
        self.min_value = min_value
        self.max_value = max_value


ACTIVE_USER = None

class User():
    '''
    Creates currently active user
    '''
    def __init__(self, email, username, custom_difficulties, current_difficulty):
        self.email = email
        self.username = username
        self.custom_difficulties = custom_difficulties
        self.current_difficulty = current_difficulty

    
    def update_username(self, username):
        '''
        Updates username and saves it to the spreadsheet
        @param self
        @param username
        '''
        #TODO: Add saving to spreadsheet and check username validity
        self.username = username

    def update_custom_difficulties(self, custom_difficulties):
        '''
        Updates custom made difficulties and saves it to the spreadsheet
        @param self
        @param custom_difficulties
        '''
        #TODO: Add saving to spreadsheet and check custom difficulty validity
        self.custom_difficulties = custom_difficulties

    def update_current_difficulty(self, current_difficulty):
        '''
        Updates current difficulty and saves it to the spreadsheet
        @param self
        @param current_difficulty
        '''
        #TODO: Add saving to spreadsheet and check difficulty validity
        self.current_difficulty = current_difficulty


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
        if self.guessing == Guesser.COMPUTER:

        self.rounds_left = self.rounds_left-1

    def start(self):
        '''
        
        '''
        self.prepare_game()



USERNAME_REGEX = "^[a-zA-Z0-9]{3,100}$"
EMAIL_REGEX = "^\S+@\S+\.\S+$"


def login() -> bool:
    '''
    Logs user in
    '''
    global ACTIVE_USER

    if ACTIVE_USER is None:
        username = ""
        email = ""
        while True:
            username = input("Please enter your username:\n")
            if re.match(USERNAME_REGEX, username):
                break
            else:
                print("Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")

        while True:
            email = input("Please enter your email:\n")
            if re.match(EMAIL_REGEX, email):
                break
            else:
                print("Please enter a valid email address")

        usersheet = SHEET.worksheet("user_list")
        email_val = usersheet.find(email)

        if not email_val is None:
            print("found")
            userrow = usersheet.row_values(email_val.row)
            ACTIVE_USER = User(userrow[0], userrow[1], userrow[2], userrow[3])
            print(userrow)
        else:
            print("This user does not exist")
            print(f"username: {username}")
            print(f"email: {email}")

            while True:
                register = input("Do you want to register with this data? Y/N\n")
                if re.search("^[yY]{1}(es)?$", register):
                    print("Register")
                    return True
                elif re.search("^[nN]{1}(o)?$", register):
                    print("Returning to the main menu")
                    return False
                else:
                    print("Incorrect input")

        #TODO: Check if user exists
        print("login check if user exists")
        return True
    else:
        print("Already logged in")
        return False



def show_register():
    '''
    Register new user
    '''
    username = ""
    email = ""
    while True:
        username = input("Please enter a username (Your username can be changed later):\n")
        if re.match(USERNAME_REGEX, username):
            break
        else:
            print("Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")

    while True:
        email = input("Please enter your email:\n")
        if re.match(EMAIL_REGEX, email):
            break
        else:
            print("Please enter a valid email address")

    usersheet = SHEET.worksheet("user_list")

_DIFFICULTIES = {
    "easy": Difficulty(5, 0 ,15),
    "medium": Difficulty(5, 0 ,15),
    "hard": Difficulty(5, 0 ,15),
    "extreme": Difficulty(5, 0 ,15),
}




OPTION_REGEX = "^[1-5]{1}$"

def show_rules(show_after):
    '''
    Displays rules than switches back to given screen after enter
    '''
    print("The rules")
    input("Press Enter to continue...")
    show_after()
    clear_console()

#Code used: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear_console():
    '''
    Clears console
    '''
    os.system('cls' if os.name=='nt' else 'clear')


def show_settings():
    '''
    Displays settings
    '''
    global ACTIVE_USER

    if ACTIVE_USER is None:
        login()
    
    print("Welcome to the settings menu")
    print('''Select one option:
1. Difficulty setting
2. Change username
3. Back to main menu''')
    while True:
        option = input("Select: ")
        if re.search(OPTION_REGEX, option):
            exit = False
            match option:
                case "1":
                    print("Show dfficulty setting")
                    break
                case "2":
                    print("change username")
                    break
                case "3":
                    main_menu()
                    break
                        
            if exit:
                break
        else:
            print("Please select the correct option")
    main_menu()
    clear_console()


def main_menu():
    '''
    Displays main menu
    '''
    print('''
Welcome to NumberGuessing

Select one option:
1. Help
2. Rules
3. Settings
4. Start game
5. Exit
    ''')
    while True:
        option = input("Select: ")
        if re.search(OPTION_REGEX, option):
            exit = False
            match option:
                case "2":
                    show_rules(main_menu)
                    break
                case "3":
                    show_settings()
                    break
                case "5":
                    while True:
                        exit_survey = input("Do want to exit the game? Y/N\n")
                        if re.search("^[yY]{1}(es)?$", exit_survey):
                            print("Goodbye")
                            exit = True
                            break
                        elif re.search("^[nN]{1}(o)?$", exit_survey):
                            break
                        else:
                            print("Incorrect input")
                        
            if exit:
                break
        else:
            print("Please select the correct option")

def main():
    '''
    Main
    '''
    main_menu()

if __name__ == "__main__":
    main()
