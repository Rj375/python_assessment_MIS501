# Create a program that ask the user to reset the password if the entered password not matched for 3 attempts.
# Note : incase of user name not matching it must advise the user to sign up.


dummyUserName = "ramesh"
dummyPassword = "123"
i = 0

while True: 
    if i == 3: #checks iF i is equal to 3 or not.
        print("You have used maximum number oF attempts, please reset your password.")
        break
    else:
        userNameInput = input("Please enter your username:- ")
        if dummyUserName != userNameInput: #checks whether dummy username and user typed username match or not.
            print("Invalid Username Please Sign Up First")
        else:
            passwordInput = input("Please enter your password:- ")

            if dummyPassword != passwordInput: #checks whether dummy password and user typed password match or not.
                i+=1 #it increases i by 1 everytime user types wrong password.
                print("Invalid Password, you have used",i,"attempts out oF 3")
            else:
                print("Welcome", dummyUserName)

# or

# Create a program that ask the user to reset the password if the entered 
# password not matched for 3 attempts.
# Note : in case of user name not matching it must advise the user to sign up.

username = ['username','username1','username2']
password = ['secretpassword','secretpassword1', 'secretpassword2']

#Attempt counter
attempts = 0 
reset_password = False
while attempts <3:
    input_username = input('Please enter your username: ')
    input_password = input('Please enter your password: ')
  
    if input_username in username:
        index = username.index(input_username)
        if input_password == password[index]:
            print('Sucessful login!')
            break
        else:
            attempts += 1
            if attempts < 3:
                print('You have entered incorrect password. Please try again.')
            if attempts == 3:
                reset_password: True
                print('You need to reset your password.')
    else:
        print('You need to register first!')
        break