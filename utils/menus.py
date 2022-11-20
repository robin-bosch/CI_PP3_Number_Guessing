
import re
import classes.User as user
import classes.ComputerGuessingGame as ComputerGuessingGame
import classes.UserGuessingGame as UserGuessingGame
import run
import utils.inputs as inputs
import utils.login as login


OPTION_REGEX = "^[1-5]{1}$"
USERNAME_REGEX = "^[a-zA-Z0-9]{3,100}$"
EMAIL_REGEX = "^\S+@\S+\.\S+$"


def main_menu():
    '''
    Displays main menu
    '''
    run.welcome()
    print('''
Welcome to NumberGuessing

Select one option:
1. Start game
2. Rules
3. Settings
4. Exit
    ''')
    while True:
        option = input("Select: ")
        if re.search(OPTION_REGEX, option):
            match option:
                case "1":
                    start_game()
                case "2":
                    show_rules(main_menu)
                case "3":
                    main_settings()
                case "4":
                    if inputs.yes_no("Do want to exit the game?"):
                        print("Goodbye")
                        break
        else:
            print("Please select the correct option")


def start_game():
    '''
    Creates game
    '''
    if login.login():
        while True:
            print('''Select one option:
1. Computer guesses
2. User guesses
3. Back to main menu''')
            option = input("Select:\n")
            if re.search(OPTION_REGEX, option):
                match option:
                    case "1":
                        new_game = ComputerGuessingGame(
                            user.get_user().current_difficulty)
                        new_game.start()
                        break
                    case "2":
                        new_game = UserGuessingGame(
                            user.get_user().current_difficulty)
                        new_game.start()
                        break
                    case "3":
                        main_menu()
            else:
                print("Please select the correct option")
    else:
        main_menu()


def manage_custom_difficulties():
    '''
    Show custom difficulties
    '''
    custom_difficulties = user.get_user().custom_difficulties

    print("Choose a difficulty to delete or add a new one")

    for index, item in enumerate(custom_difficulties):
        print(f'''{str(index+1)}. {item.name} - \
Rounds: {str(item.rounds)} - \
Min value: {str(item.min_value)} - \
Max value: {str(item.max_value)}''')

    print(f"{str(len(custom_difficulties)+1)}. Add a new custom difficulty")

    custom_option_regex = "^[1-" + str(len(custom_difficulties)) + "]{1}$"
    while True:
        option = input("Select: ")
        if re.search(custom_option_regex, option):
            option = int(option)

            if option+2 == len(custom_difficulties):
                main_settings()
            else:
                print(f'''{custom_difficulties[option-1].name} - \
Rounds: {str(custom_difficulties[option-1].rounds)} - \
Min value: {str(custom_difficulties[option-1].min_value)} - \
Max value: {str(custom_difficulties[option-1].max_value)}''')

                confirm_delete = inputs.yes_no("Do you want to delete this custom difficulty?")

                if confirm_delete:
                    print("Deleting")
                else:
                    manage_custom_difficulties()
        else:
            print("Please select the correct option")


def add_custom_difficulty():


def change_difficulty():
    '''
    Changes current difficulty
    '''
    difficulty_list = run._DIFFICULTIES
    difficulty_list.append(user.get_user().custom_difficulties)

    for index, item in enumerate(difficulty_list):
        print(f"{str(index+1)}. {item.name} - Rounds: {item.rounds} - Min value: {item.min_value} - Max value: {item.max_value}")


def rules():
    '''
    Displays rules than switches back to given screen after enter
    '''
    print("The rules")
    input("Press Enter to continue...")
    main_menu()


def change_username_setting():
    '''
    Asks for new username and calls the update
    username function in the user object
    '''
    while True:
        new_username = input("Please enter your new username:\n")
        if new_username == "exit":
            main_settings()
            break
        elif re.match(USERNAME_REGEX, new_username):
            user.get_user().update_username(new_username)
            print("Username changed")
            main_settings()
            break
        else:
            print("Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")


def main_settings():
    '''
    Displays settings
    '''

    if login.login():
        print("Settings menu")

        while True:
            print('''Select one option:
1. Change difficulty
2. Change username
3. Manage custom difficulties
4. Back to main menu''')
            option = input("Select: ")
            if re.search(OPTION_REGEX, option):
                exit = False
                match option:
                    case "1":
                        change_difficulty()
                        break
                    case "2":
                        change_username_setting()
                        break
                    case "3":
                        manage_custom_difficulties()
                        break
                    case "4":
                        main_menu()
                        break

                if exit:
                    break
            else:
                print("Please select the correct option")
    else:
        main_menu()
