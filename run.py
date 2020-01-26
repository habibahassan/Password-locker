from user import User
import string
import random
import getpass
from password import password

def create_password(account_name, passkey):
    '''
    function to create a new password
    '''
    new_password = password(account_name, passkey)
    return new_password
def save_password(password):
    '''
    function to save a password
    '''
    password.save_password()
def display_passwords():
    '''
    function that dispalys all passwords
    '''
    return password.display_passwords()
def delete_password(password):
    '''
    function to delete a password
    '''
    password.delete_password()
def check_existing_user(password2):
    '''
    function to check that enable login authentification
    '''
    return User.user_exist(password2)
def find_account(password2):
    '''
    function to find account by its name
    '''
    return User.find_account(password2)




