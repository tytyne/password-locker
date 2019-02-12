

class credentials:


    credentials_list = [] # Empty credentials list



    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        credentials.credentials_list.append(self)

    def __init__(self,username,pas):
        self.username="admin"
        self.pas="admin123"

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        credentials.credentials_list.remove(self)



    