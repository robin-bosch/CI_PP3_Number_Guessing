import re
import os

class Difficulty():
    '''
    Creates a difficulty
    '''
    def __init__(self, rounds, min, max):
        self.rounds = rounds
        self.min = min
        self.max = max


DIFFICULTIES = {
    "easy": Difficulty(5, 0 ,15),
    "medium": Difficulty(5, 0 ,15),
    "hard": Difficulty(5, 0 ,15),
    "extreme": Difficulty(5, 0 ,15),
}




regex = "^[1-5]{1}$"

def show_rules(showAfter):
    '''
    Displays rules than switches back to given screen after enter
    '''
    print("The rules")
    input("Press Enter to continue...")
    showAfter()
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
        if re.search(regex, option):
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
    main_menu()

if __name__ == "__main__":
    main()
