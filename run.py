import json
import random
import re
import os

from classes.ComputerGuessingGame import ComputerGuessingGame
from classes.User import User
from classes.UserGuessingGame import UserGuessingGame
from utils.inputs import take_text_input, yes_no
from utils.worksheet import USER_LIST


# from game import ComputerGuesserGame, UserGuesserGame





class Difficulty():
    '''
    Creates a difficulty
    '''
    def __init__(self, rounds, min_value, max_value):
        self.rounds = rounds
        self.min_value = min_value
        self.max_value = max_value

_DIFFICULTIES = {
    "easy": Difficulty(5, 0 ,15),
    "medium": Difficulty(5, 0 ,15),
    "hard": Difficulty(5, 0 ,15),
    "extreme": Difficulty(5, 0 ,15),
}

ACTIVE_USER = None


USERNAME_REGEX = "^[a-zA-Z0-9]{3,100}$"
EMAIL_REGEX = "^\S+@\S+\.\S+$"

def is_logged_in() -> bool:
    '''
    Checks if the user is logged in
    '''
    return False if ACTIVE_USER is None else True

def start_game():
    if is_logged_in():
        while True:
            print('''Select one option:
1. Computer guesses
2. User guesses
3. Back to main menu''')
            option = input("Select: ")
            if re.search(OPTION_REGEX, option):
                match option:
                    case "1":
                        new_game = ComputerGuessingGame(_DIFFICULTIES[ACTIVE_USER.current_difficulty])
                        new_game.start()
                        break
                    case "2":
                        new_game = UserGuessingGame(_DIFFICULTIES[ACTIVE_USER.current_difficulty])
                        new_game.start()
                        break
                    case "3":
                        main_menu()
            else:
                print("Please select the correct option")
    else:
        print("You are not logged in")
        login_prompt = yes_no("You need to login to play, do you want to login? Y/N\n")

        if login_prompt:
            login()
            start_game()
        else:
            main_menu()




def login() -> bool:
    '''
    Logs user in
    '''
    global ACTIVE_USER

    if not is_logged_in():

        registered = yes_no("Are you registered? Y/N\n")

        if registered:

            username = take_text_input("Please enter your username", USERNAME_REGEX, "Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")
            email = take_text_input("Please enter your email", EMAIL_REGEX, "Invalid email address, please enter a valid email address")
            # # Take username input
            # while True:
            #     username = input("Please enter your username:\n")
            #     if re.match(USERNAME_REGEX, username):
            #         break
            #     else:
            #         print("Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")
            # # Take email input
            # while True:
            #     email = input("Please enter your email:\n")
            #     if re.match(EMAIL_REGEX, email):
            #         break
            #     else:
            #         print("Please enter a valid email address")

            # usersheet = SHEET.worksheet("user_list")
            email_val = USER_LIST.find(email)

            if not email_val is None:
                print("found")
                userrow = USER_LIST.row_values(email_val.row)
                ACTIVE_USER = User(email_val.row, userrow[0], userrow[1], userrow[2], userrow[3])
                print(userrow)
            else:
                print("This user does not exist")
                print(f"username: {username}")
                print(f"email: {email}")

                if yes_no("Do you want to register with this data? Y/N\n"):
                    print("Register")
                    USER_LIST.append_row([email, username, "{}", "easy"])
                    userrow_num = USER_LIST.find(email)
                    userrow_val = USER_LIST.row_values(userrow_num.row)
                    ACTIVE_USER = User(userrow_num.row, userrow_val[0], userrow_val[1], userrow_val[2], userrow_val[3])
                    return True
                else:
                    print("Returning to the main menu")
                    return False

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






OPTION_REGEX = "^[1-5]{1}$"

def show_custom_difficulties():
    '''
    Show custom difficulties
    '''
    print("Choose a difficulty to delete or add a new one")
    difficulty_list = json.loads(ACTIVE_USER.custom_difficulties)
    for key in json.loads(ACTIVE_USER.custom_difficulties).keys():
        print(f"1. {key} - Rounds: {difficulty_list[key][0]} - Min value: {difficulty_list[key][1]} - Max value: {difficulty_list[key][2]}")

    while True:
        option = input("Select: ")
        if re.search(OPTION_REGEX, option):
            match option:
                case "1":
                    print("Change difficulty coming")
                    break
                case "2":
                    change_username_setting()
                    break
                case "3":
                    show_custom_difficulties()
                    break
                case "4":
                    main_menu()
                    break
        else:
            print("Please select the correct option")

    print()


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

def change_username_setting():
    '''
    Asks for new username and calls the update username function in the user object
    '''
    while True:
        new_username = input("Please enter your new username:\n")
        if new_username == "exit":
            show_settings()
            break
        elif re.match(USERNAME_REGEX, new_username):
            ACTIVE_USER.update_username(new_username)
            print("Username changed")
            show_settings()
            break
        else:
            print("Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")

def show_settings():
    '''
    Displays settings
    '''
    global ACTIVE_USER

    if ACTIVE_USER is None:
        login()
    
    print("Welcome to the settings menu")
    print(
'''Select one option:
1. Change difficulty
2. Change username
3. Manage custom difficulties
4. Back to main menu''')

    while True:
        option = input("Select: ")
        if re.search(OPTION_REGEX, option):
            exit = False
            match option:
                case "1":
                    print("Change difficulty coming")
                    break
                case "2":
                    change_username_setting()
                    break
                case "3":
                    show_custom_difficulties()
                    break
                case "4":
                    main_menu()
                    break
                        
            if exit:
                break
        else:
            print("Please select the correct option")
    main_menu()
    clear_console()

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


def main_menu():
    '''
    Displays main menu
    '''
    welcome()
    print('''
Welcome to NumberGuessing

Select one option:
1. Start game
2. Help
3. Rules
4. Settings
5. Exit
    ''')
    while True:
        option = input("Select: ")
        if re.search(OPTION_REGEX, option):
            match option:
                case "1":
                    start_game()
                case "2":
                    print("Help is coming! At some point...")
                case "3":
                    show_rules(main_menu)
                case "4":
                    show_settings()
                case "5":
                    if yes_no("Do want to exit the game?"):
                        print("Goodbye")
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
