# Create a program that ask the user to enter email id. 
# The program must show the user a message of "correct format of email", 
# if the email has all letters and one @ with minimum of 25 characters.

import re

regEx = re.compile(r'^[a-zA-Z@]{25}$') #its a regular expression For valid email id.

while True:
    userInput = input("Please enter your email address:- ")

    isValidEmail = re.search(regEx, userInput) #validates the userInput with the regular expression.

    if isValidEmail == None: #checks whether the email id is None or not.
        print("Please enter correct Format oF email id.")
    else:
        print("the email id is in correct Format and your email is:-", userInput)
        exit()

