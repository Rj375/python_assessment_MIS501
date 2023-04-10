# Write a code for user to enter his name and dob where the system will confirm the valid credentials i
# if the name has first and last name (I.e. includes a space), 
# and dob with 2 "/" ( I.e. 01/06/1990.)
import re


userNameInput = "Please enter your First and Last Name with spaces:- "
dateOfBirthInput = "Please enter you date oF birth (DD/MM/YYYY):- "
errorMessage = "Please enter valid credentials (Full Name with space and dob (DD/MM/YYYY))"

dateFormat = re.compile(r'^\d{2}/\d{2}/\d{4}$') #its a regular expression For valid date Foramt.


while True:
    userName = input(userNameInput)
    dateOfBirth = input(dateOfBirthInput)

    dob = re.search(dateFormat, dateOfBirth) #checks the validity of the date Format with date input.
    isSpace = userName.count(" ") #checks whether the user has name with space or not.

    if isSpace == 1 and dob: #check whether isSpace and dob has valid value or not.
        splittedValue = userName.split() #it splits input values and return as list.
        capitalizedFirstName = splittedValue[0].capitalize() #capitalized first name oF user.
        capitalizedLastName = splittedValue[1].capitalize() #same as above but with last name.
        print("Your Full Name is", capitalizedFirstName, capitalizedLastName)
        print("Your date oF birth is", dateOfBirth)
        exit()    
    else:
        print(errorMessage)