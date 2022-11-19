import re
import utils.inputs as inputs
import utils.worksheet as worksheet
import utils.menus as menus
import classes.User as user


OPTION_REGEX = "^[1-5]{1}$"
USERNAME_REGEX = "^[a-zA-Z0-9]{3,100}$"
EMAIL_REGEX = "^\S+@\S+\.\S+$"


def is_logged_in() -> bool:
    '''
    Checks if the user is logged in
    '''
    return False if user.get_user() is None else True


def login() -> bool:
    '''
    Logs user in
    '''
    # global user

    if not is_logged_in():

        while True:
            print('''You need to be logged in to access this area.\n
1. Log In
2. Register
3. Retun to the main menu        
''')
            user_choice = input("Select:\n")

            if re.search("^[1-3]{1}$", user_choice):
                match user_choice:
                    case "1":
                        username = inputs.take_text_input("Please enter your username", USERNAME_REGEX, "Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")
                        email = inputs.take_text_input("Please enter your email", EMAIL_REGEX, "Invalid email address, please enter a valid email address")

                        return_user = worksheet.query_user(email)

                        if return_user is not None:
                        # if not email_val is None:
                            # Login user
                            # userrow = USER_LIST.row_values(email_val.row)
                            # user_difficulties = json.loads(userrow[2])

                            # query_user(email)

                            # print(user_difficulties)

                            custom_difficulty_list = {}

                            # for key in user_difficulties.items():
                            #     print(user_difficulties[key])
                            #     custom_difficulty_list[key] = Difficulty(user_difficulties[key][0], user_difficulties[key][1], user_difficulties[key][2])

                            print(return_user)

                            user.set_user(return_user)

                            print(user)
                            return True
                        else:
                            #
                            print("This user does not exist")
                            print(f"username: {username}")
                            print(f"email: {email}")

                            if inputs.yes_no("Do you want to register with this data?"):
                                # USER_LIST.append_row([email, username, "{}", "easy"])
                                # userrow_num = USER_LIST.find(email)
                                # userrow_val = USER_LIST.row_values(userrow_num.row)
                                # from classes.User import User
                                # user = User(userrow_num.row, userrow_val[0], userrow_val[1], userrow_val[2], userrow_val[3])
                                return True
                            else:
                                # Returns to the login main screen
                                login()
                    case "2":
                        # show_register()
                        return True
                    case "3":
                        menus.main_menu()
                        return False
            else:
                print("Please select the correct option")
    return True



# def show_register():
#     '''
#     Register new user
#     '''
#     global ACTIVE_USER

#     username = take_text_input("Please enter a username (Your username can be changed later)", USERNAME_REGEX, "Your username must be 3-100 Characters long and can only contain alphanumeric values (A-Z and 0-9)")
#     email = take_text_input("Please enter your email", EMAIL_REGEX, "Invalid email address, please enter a valid email address")

#     email_val = USER_LIST.find(email)

#     if email_val is None:
#         USER_LIST.append_row([email, username, "{}", "easy"])
#         userrow_num = USER_LIST.find(email)
#         userrow_val = USER_LIST.row_values(userrow_num.row)
#         ACTIVE_USER = User(userrow_num.row, userrow_val[0], userrow_val[1], userrow_val[2], userrow_val[3])
#     else:
#         print("This user already exists please register as new user")
#         login()