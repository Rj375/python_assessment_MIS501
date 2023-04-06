# Create a program to ask the user to enter his full name and then print the message greeting the user with his first and last name individually.
# The program must tell the user if the name has no surname or more than 2 part of names.
# Example
# Sam John
# Accepted
# SamJohn and Sam Andrew John not accepted



inputPlaceHolder = "Please enter your First and Last Name with spaces:- "
while True:
    userInput = input(inputPlaceHolder)

    isSpace = userInput.count(" ") #checks whether the user has name with space or not.

    if isSpace == 1: #check whether isSpace has valid value or not.
        splittedValue = userInput.split() #it splits input values and return as list.
        capitalizedFirstName = splittedValue[0].capitalize() #capitalized first name oF user.
        capitalizedLastName = splittedValue[1].capitalize() #same as above but with last name.
        print("Your Full Name is", capitalizedFirstName, capitalizedLastName)
        exit()
    elif len(userInput.split()) >= 3: #check whether the name has more than 3 length or not.
        print("Only First Name and Last Name are allowed")
    else:
        print(inputPlaceHolder)

