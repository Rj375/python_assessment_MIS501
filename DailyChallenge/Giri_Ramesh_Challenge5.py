# Create a program that ask the user to enter his year of birth and print whether he can create an account or not.
# Condition : minimum age to create an account is 18 years.

from datetime import datetime

#it shows the present year which is 2023.
presentYear = datetime.today().year

yearOfBirth = int(input("Please enter your year of birth:- "))

#it substracts present year with the year that user typed.
currentAge = presentYear - yearOfBirth

if currentAge >= 18:
    print("Congratulations, you are eligible to create account. Thank you.😃")
else:
    print("Oops, you are not eligible to create account. Sorry.😞")

