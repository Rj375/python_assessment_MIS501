mobile_phone = input("Insert your phone number")
password = input("Enter your password")



if len(mobile_phone) == 10 and len(password) >= 8:
    print("Valid Credentials")
else:
    print("Invalid Credentials")
