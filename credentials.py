

class credentials:

    credentials_list = []  # Empty credentials list

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        credentials.credentials_list.append(self)

    def __init__(self, username, pas):
        self.username = "admin"
        self.pas = "admin123"

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        credentials.credentials_list.remove(self)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the login crentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = credentials("Admin", "admin123")  # new credentials
        test_credentials.save_credentials()

        credentials_exists = credentials.credentials_exist(
            "yes the login credentials are saved")

        self.assertTrue(credentials_exists)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user list
        '''
        return cls.credentials_list
