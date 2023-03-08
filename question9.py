mobilePhone = input("Insert your phone number")
password = input("Enter your password")


#it checks where the mobilePhone has exactly 10 digits and where the length oF password is greater than or equal to 8.
if len(mobilePhone) == 10 and len(password) >= 8:
    print("Valid Credentials")
else:
    print("Invalid Credentials")