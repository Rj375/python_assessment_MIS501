# Create a program that advise the user to enter a correct password of 8 character and with numbers and letters for 3 attempts.
# After 3 attempts it must ask the user to reset the password.
import re

PasswordRegex = re.compile(r'^[A-Za-z0-9]{8,}$') #regular expression for password


for i in range(3):
    userInput = input("Please enter your password with atleast 8 characters and should contain numbers and letters:- ")
    isPasswordValid = re.search(PasswordRegex, userInput) #validates reg ex with userinput.
    i+=1 #increases i by 1.
    if isPasswordValid: #checks whether reg ex is valid or not.
        print("Your password is:-",userInput)
        break
    elif i == 3: #checks whether i is equal to 3 or not.
        print("You have used maximum number oF attempts, Please reset your password")
    else:
        print("Wrong password Format, Please try again, you have used",i,"out oF 3 attempts")

        
    
