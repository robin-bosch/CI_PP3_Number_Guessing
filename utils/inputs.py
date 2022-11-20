import re

# custom imports
import utils.menus as menus


def yes_no(question) -> bool:
    '''
    Display simple yes or no question in the terminal
    '''
    while True:
        register = input(question + "Y/N\n")
        if re.search("^[yY]{1}(es)?$", register):
            return True
        elif re.search("^[nN]{1}(o)?$", register):
            return False
        else:
            print("Incorrect input")


def take_text_input(input_prompt, check_regex, failure_message) -> str:
    '''
    Takes the input with a given regex
    '''
    while True:
        input_val = input(input_prompt +
                          " or exit to get back to the main menu:\n")
        if input_val == "exit":
            menus.main_menu()
        elif re.match(check_regex, input_val):
            return input_val
        else:
            print(failure_message)
