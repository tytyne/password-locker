import unittest # Importing the unittest module
import pyperclip
from user import user # Importing the user class



class Testuser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("James","Muriuki","0712345678","james@ms.com") # create user object


    def test_init(self):
         '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"james@ms.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(user.user_list),1)


# setup and clacontacttion up herecontact
    def tearDowuser:user
            '''contactcontact
            tearDown method that does userclean up after each test case has run.
            '''
            user.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = user("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(user.user_list),2)


# More testuser
    def tesuserntact(self):
           user
           usere_user to test if we can remove a user from our user list
           user
           userontact.save_user()
           userct = user("Test","user","0712345678","test@user.com") # new user
           userct.save_user()

          userontact.delete_user()# Deleting a user object
           usertEqual(len(user.user_list),1)

def test_fiuserby_number(self):
        '''user
        tesuserif we can find a user by phone number and display information
        '''user

        self.new_user.save_user()
        test_user = user("Test","user","0711223344","test@user.com") # new user
        test_user.save_user()

        found_user = user.find_by_number("0711223344")

 
 
        self.assertEqual(found_user.email,test_user.email)
@classmethod
def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            user of person that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user
@classmethod
def user_exist(cls,number):
        '''
        Method that checks if a userexists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                    return True

        return False

def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(user.display_users(),user.user_list)

def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user
        '''

        self.new_user.save_user()
        user.copy_email("0712345678")

        self.assertEqual(self.new_user.email,pyperclip.paste())        
@classmethod
def copy_email(cls,number):
        user_found = user.find_by_number(number)
        pyperclip.copy(user_found.email)

if __name__ == '__main__':
    unittest.main()