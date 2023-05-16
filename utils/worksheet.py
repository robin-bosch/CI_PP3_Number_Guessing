import gspread
from google.oauth2.service_account import Credentials

from classes.CustomDifficulty import CustomDifficulty
from run import _DIFFICULTIES

# from classes.User import User

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('number_guessing')

USER_LIST = SHEET.worksheet("user_list")
CUSTOM_DIFFICULTIES = SHEET.worksheet("custom_difficulties")


def query_user(email):
    '''
    Querys for user in spreadsheet and returns user if available
    '''
    # Find user
    user_query = USER_LIST.find(email)

    # User exists
    if user_query is not None:
        # Login user
        userrow = USER_LIST.row_values(user_query.row)

        # Get custom difficulty list
        custom_difficulty_list = get_custom_difficulty_list(email)

        # Find active difficulty
        active_difficulty = None

        for item in _DIFFICULTIES:
            if item.name == userrow[2]:
                active_difficulty = item
                break

        if active_difficulty is None:
            for item in custom_difficulty_list:
                if item.name == userrow[2]:
                    active_difficulty = item
                    break

        from classes.User import User
        return User(user_query.row, userrow[0], userrow[1],
                    custom_difficulty_list, active_difficulty)
    else:
        # User does not exist
        return None


def get_custom_difficulty_list(email):
    '''
    Gets the list with custom difficulties
    '''
    # Create custom difficulty list
    custom_difficulty_query_list = CUSTOM_DIFFICULTIES.findall(email)

    custom_difficulty_list = []

    for item in custom_difficulty_query_list:
        difficulty_row = CUSTOM_DIFFICULTIES.row_values(item.row)
        custom_difficulty_list.append(CustomDifficulty(item.row,
                                                       difficulty_row[1],
                                                       int(difficulty_row[2]),
                                                       int(difficulty_row[3]),
                                                       int(difficulty_row[4])))

    return custom_difficulty_list


def add_custom_difficulty_row(username, name, rounds, min, max):
    '''
    Adds the custom difficulty to the table
    '''
    CUSTOM_DIFFICULTIES.append_row([username, name, rounds, min, max])


def delete_custom_difficulty_row(row):
    '''
    Deletes a custom difficulty from the table
    '''
    CUSTOM_DIFFICULTIES.delete_rows(row)
