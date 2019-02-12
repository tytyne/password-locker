
from user import user
from credentials import credentials

def login_credentials(xusername,xpassword):
'''
    Function to create login credentials
    '''

    new_credentials = credentials(xusername,xpassword)
    return new_credentials
    def save_credentials(credentials):


credentials.save_credentials()
def del_credentials(credentials):
    '''
    Function to delete a user
    '''
    credentials.delete_credentials()

def create_user(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = user(fname,lname,phone,email)
    return new_user
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return user.find_by_number(number)  
def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return user.user_exist(number)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return user.display_users()
def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : bc - create username and password cc - create email, dc - display users, fc -find a user, ex -exit the user list ")

        short_code = input().lower()

if short_code == 'bc':
            print("New user enter  your login credentials")
            print("-"*10)

            print ("Username....")
          xusername = input()

            print("Password ...")
            xpassword = input() #for login credentials

        elif short_code == 'cc':
            print("New user")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()
            save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new user.
            print ('\n')
            print(f"New user {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':

                    if display_users():
                        print("Here is a list of all your users")
                        print('\n')

                    for user in display_users():
                        print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                        print('\n')
                    else:
                        print('\n')
                        print("You dont seem to have any users saved yet")
                        print('\n')

     
        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_users(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)
                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That user does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()