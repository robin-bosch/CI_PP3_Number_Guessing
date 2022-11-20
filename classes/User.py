import utils.worksheet as worksheet


class User():
    '''
    Creates currently active user
    '''
    def __init__(self, row, email, username,
                 custom_difficulties, current_difficulty):
        self.row = row
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
        worksheet.USER_LIST.update_cell(self.row, 2, username)
        self.username = username

    def update_custom_difficulties(self, username, name, rounds, min, max):
        '''
        Updates custom made difficulties and saves it to the spreadsheet
        @param self
        @param custom_difficulties
        '''
        worksheet.add_custom_difficulty_row(username, name, rounds, min, max)
        self.custom_difficulties = worksheet.get_custom_difficulty_list(self.email)

    def update_current_difficulty(self, new_current_difficulty):
        '''
        Updates current difficulty and saves it to the spreadsheet
        @param self
        @param current_difficulty
        '''
        worksheet.USER_LIST.update_cell(self.row, 3, new_current_difficulty.name)
        self.current_difficulty = new_current_difficulty


USER = None


def get_user():
    return USER


def set_user(new_user):
    global USER
    USER = new_user
