
import re
import time

# Custom imports
import run
import classes.User as user
import utils.inputs as inputs
import utils.worksheet as worksheet
import utils.menus as menus


OPTION_REGEX = "^[1-5]{1}$"
USERNAME_REGEX = "^[a-zA-Z0-9]{3,100}$"
EMAIL_REGEX = r"^\S+@\S+\.\S+$"


def is_logged_in() -> bool:
    '''
    Checks if the user is logged in
    '''
    return False if user.get_user() is None else True


def login() -> bool:
    '''
    Logs user in
    '''
    if not is_logged_in():

        while True:
            run.clear()
            print(r'''
   __             _
  / /  ___   __ _(_)_ __
 / /  / _ \ / _` | | '_ \
/ /__| (_) | (_| | | | | |
\____/\___/ \__, |_|_| |_|
            |___/
            ''')
            print('''You need to be logged in to access this area.\n
1. Log In
2. Register
3. Return to the main menu
''')
            user_choice = input("Select:\n")

            if re.search("^[1-3]{1}$", user_choice):
                match user_choice:
                    case "1":
                        email = inputs.take_text_input(
                                "Please enter your email",
                                EMAIL_REGEX,
                                "Invalid email address, \
                                please enter a valid email address")

                        return_user = worksheet.query_user(email)

                        if return_user is not None:
                            user.set_user(return_user)
                            return True
                        else:
                            # User does not exist
                            print("This user does not exist")
                            input("Press enter to return to the login screen")
                            login()
                    case "2":
                        register()
                        return True
                    case "3":
                        menus.main_menu()
            else:
                print("Please select the correct option")
                time.sleep(2)
    return True


def register():
    '''
    Register new user
    '''
    username = inputs.take_text_input(
               "Please enter a username (Your username can be changed later)",
               USERNAME_REGEX,
               "Your username must be 3-100 Characters long and \
               can only contain alphanumeric values (A-Z and 0-9)")
    email = inputs.take_text_input(
            "Please enter your email",
            EMAIL_REGEX,
            "Invalid email address, please enter a valid email address")

    email_val = worksheet.USER_LIST.find(email)

    if email_val is None:
        worksheet.USER_LIST.append_row([email, username, "easy"])
        user.set_user(worksheet.query_user(email))
    else:
        print("This user already exists please register as new user")
        login()
