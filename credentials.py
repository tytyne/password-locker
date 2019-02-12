
import re 
class credentials
   password_list = []
  def get_password(self):
    password.password_list.append(self)

 def __init__(self,psswrd):

     

        self.psswrd = psswrd



password = "demo123"
flag = 0
while True:   
    if (len(password)<8): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid Password") 
        break
  
if flag ==-1: 
    print("Not a Valid Password") 