# Create a program that advise the user to enter name and mobile number of 3 users and save them in the lists.
# Then the user must be asked to enter 1 mobile number and the program must show the name of the associated user with a greeting message.
# Incase of new number the message must be shown I.e. no data with this number in the records.
import re

listOfData = []

for i in range(3):
    userDetails = []
    userName = input("Please enter your name:- ")
    userMobileNumber = input("Please enter your mobile number:- ")
   
    userDetails.append(userName) #adds userName in userDetails list.
    userDetails.append(userMobileNumber) #adds userMobileNumber in userDetails list.

    listOfData.append(userDetails) #adds userDetails list in data listOfData.

userLoginInputMobileNumber = input("Please enter your mobile number to login:- ")

for items in listOfData:
    if items[1] == userLoginInputMobileNumber: #checks whether user login input matches with items or not.
        print("Hi", items[0]) 
        break
    else:
        print("Number you entered does not exist in record")
        break


