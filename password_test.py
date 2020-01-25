import unittest

from password import password


class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_password = password("twitter", "swift")
    def test_save_password(self):
        '''
        test_save_password tests if a new password has been added to passwords
        list of a user
        '''
        self.new_password.save_password()
        self.assertEqual(len(password.password_list), 3)    
    def test_display_passwords(self):
        '''
        test to display the passwords of a user
        '''
        self.assertEqual(password.display_passwords(),
                         password.password_list)
    def test_delete_password(self):
        '''
        test_delete_password to see if we can remove a 
        password from passwords list
        '''
        self.new_password.save_password()
        test_password = password("test", "5921fszju")
        test_password.save_password()

        self.assertEqual(len(password.password_list), 2)

if __name__ ==  '__main__':
    unittest.main()