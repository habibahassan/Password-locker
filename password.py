class password:
    """
    Class that generates new instances of password
    """
    password_list = [] # Empty password list
    def save_password(self):
        '''
        save_password method saves object in password list
        '''
        password.password_list.append(self)

    def __init__(self, account_name, passkey):
        self.account_name = account_name
        self.passkey = passkey

    @classmethod
    def display_passwords(cls):
        '''
        method that returns password of a user
        '''
        return cls.password_list
    @classmethod
    def delete_password(cls, account):
        '''
        delete a password
        '''
        for password in cls.password_list:
            if password.account_name == account:
                return password