import re
import os
from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials


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


active_user = None

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
    print("Settings are coming")
    input("Press Enter to continue...")
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
