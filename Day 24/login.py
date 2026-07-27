class Createaccount :
    def __init__(self,username , password):
        self.username = username 
        self.password = password 

class Loginnow :
    def __init__(self,name , passw):
            self.name = name 
            self.passw = passw 

print('Create your Account')
username = input('Input username : ')
password = input('Input password : ')
person1 = Createaccount(username ,password)
print(f"User '{username}' created successfully ")
print()

print('Login now')
name = input('Input username : ')
passw = input('Input password : ')
person1_logged = Loginnow(name , passw)

if person1.username == person1_logged.name and person1.password == person1_logged.passw :
     print('User Logged in successfully')
else:
     print('Invalid credentials')