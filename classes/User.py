from utils.worksheet import USER_LIST


class User():
    '''
    Creates currently active user
    '''
    def __init__(self, row, email, username, custom_difficulties, current_difficulty):
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
        USER_LIST.update_cell(self.row, 2, username)
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
        USER_LIST.update_cell(self.row, 4, current_difficulty)
        self.current_difficulty = current_difficulty