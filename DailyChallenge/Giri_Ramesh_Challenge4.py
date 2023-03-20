# Create a program that ask the user to enter user name and password and print the output of successful login and unsuccessful login.
# Note - The program must display the issue related to unsuccessfully login I.e. wrong password or invalid username.

username = "Ramesh"
password = "Giri75"

#this program checks validation the moment user types username and password one by one.
#if any oF the condition mentioned doesn't meet, then program will exit.
givenUserName = input("Please enter your username:- ")
if username != givenUserName:
    print("The username you typed is invalid")
    exit()

givenPassword = input("Please enter your password:- ")
if password != givenPassword:
    print("The password you typed is invalid")
    exit()

print("successfully logged in")

#or you can also do like this.
# if username != givenUserName:
#     print("The username you typed is invalid")
# elif password != givenPassword:
#     print("The password you typed is invalid")
# else:
#     print("SuccesFully logged in")

    