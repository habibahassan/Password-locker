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
def create_user(f_name, s_name, password):
    '''
    function to create a new user
    '''
    new_user = User(f_name, s_name, password)
    return new_user

def save_users(user):
    '''
    function to save a user
    '''
    user.save_user()

def display_users(user):
    '''
    function to find users by there name
    '''
    return User.display_users()

def introduction():
    print("Hey! Welcome to Password Locker")
    print('\n')
    print("Please sign up for an accout to enjoy services")

    while True:
        print("Use these short codes : su - Sign up, lg - login, du-display all users, ex-Exit app ")
        print('-'*64)
        print('\n')
        short_code = input().lower()
        print('\n')
        if short_code == 'su':
            print("New User")
            print("-"*9)

            print("Enter you first name...")
            f_name = input()

            print("Enter your second name...")
            s_name = input()

            print("Enter your password...")
            password = input()
            print('\n')

            save_users(create_user(f_name, s_name, password))
            print('\n')
            print(
                f"Congratulations {f_name} {s_name}, you now have an account \n")
            print('\n')
        elif short_code == 'lg':

            print("Enter the first name of your registered account")
            account_name = input()
            print('\n')

            authentification = getpass.getpass('Password:')
            if check_existing_user(authentification):
                search_account = find_account(authentification)

                while True:
                    print(
                        f"Welcome {search_account.first_name} {search_account.second_name} \n")
                    print(
                        "cc-To create new password, vc-To view all your passwords, ex-exit account \n ")
                    print('-'*80)
                    short_code = input().lower()
                    if short_code == 'cc':
                        print("New password")
                        print('-'*14)
                        print("Enter account name")
                        account_name = input()
                        print("Make a password \n")
                        print(
                            "To make your own password press- a, to generate a password press - g \n")
                        print('-'*50)
                        generate = input()
                        print('\n')

                        if generate == 'g':
                            letters = string.ascii_letters + string.digits
                            gpassword = ''.join(random.choice(letters)
                                                for i in range(9))
                            print(
                                f"Your new generated password is: {gpassword} \n")
                            passkey = gpassword

                        elif generate == 'a':
                            print("Enter its password")
                            print('\n')
                        print(f"{account_name} has been saved")
                        passkey = input()
                        save_password(create_password(
                            account_name, passkey))

                    elif short_code == 'vc':
                        if display_passwords:
                            print(
                                "Here is a list of all your accounts and passwords \n")
                            for password in display_passwords():
                                print(
                                    f"Account name: {password.account_name} - password: {password.passkey}")
                    elif short_code == 'dc':
                        print("Which password would you like to delete?")
                        del_account = input()
                        if del_account == account_name:

                            password.password_list.remove(password)
                            print("password deleted")
                        else:
                            print("No match this password")

                    elif short_code == 'ex':
                        print("You have exited your account \n")
                        break
            else:
                print("The password was incorrect \n")
                print('\n')
        elif short_code == 'du':
            print("Here is a list of all the users\n")
            for users in display_users():
                print(f"{user.first_name} {user.second_name} \n")

        elif short_code == 'ex':

            print("Ok well. hope to see you again! \n")

            break
        else:
            print("I cant understand this, please use these codes \n")


if __name__ == '__main__':

    introduction()
    