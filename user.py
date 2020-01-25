from password import password
class User:
    '''
    class that generates new instances of users accounts
    '''
    user_list = []  # user list
    def save_user(self):
        '''
        save_user method saves users
        '''
        User.user_list.append(self)
     def __init__(self, first_name, second_name, password):

       # create new user instance

        self.first_name = first_name
        self.second_name = second_name
        self.password = password
    @classmethod
    def display_users(cls):
        '''
        method to display all the users
        '''
        return cls.user_list
     @classmethod
    def user_exist(cls, password):
        '''
        method to check if a user and
        their details exist
        '''
        for user in cls.user_list:
            if user.password == password:
                return True
        return False

    # @classmethod
    # def find_account(cls, password2):
    #     '''
    #     method that finds an account by its name
    #     '''
    #     for user in cls.user_list:
    #         if user.password == password2:
    #             return user