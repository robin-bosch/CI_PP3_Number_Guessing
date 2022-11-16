import re
import os

DIFFICULTIES = {
    "easy": {
        "rounds": 5,
        "min": 0,
        "max": 10
    },
    "medium": {
        "rounds": 10,
        "min": 0,
        "max": 10
    },
    "hard": {
        "rounds": 5,
        "min": 0,
        "max": 10
    },
    "extreme": {
        "rounds": 5,
        "min": 0,
        "max": 10
    }
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
            match option:
                case "2":
                    show_rules(main_menu)
                    break
            break
        else:
            print("Please select the correct option")

def main():
    main_menu()

if __name__ == "__main__":
    main()
