# Create a program that advise the user to enter the correct password for 3 attempts.
# If password is all digit entered:
# Output : The password must include alphabets as well.
# If password is all alphabets:
# Output: The password must include digits as well.
# If password is less than 8 character long.
# Output: The password be atleast 8 character long.
# If all conditions satisfied.
# Output: correct format of password.



counter = 3

while counter > 0: #loop executes untill the counter is greater than 0.
    userPassword = input("Enter the password:- ")
    
    if userPassword.isdigit(): #checks whether the password contains all the numbers or not.
        print("The password must include alphabets as well.")
    elif userPassword.isalpha(): #checks whether the password contains all the alphabets or not.
        print("The password must include digits as well.")
    elif len(userPassword) < 8: #checks whether the password length is not less than 8 characters.
        print("The password should be atleast 8 characters long.")
    else:
        print("Correct format of password.")
        break
        
    counter -= 1 #decreases counter by 1.
    if counter == 0: #iF counter is equal to 0, then it means user has used all the attempts leFt.
        print("You have used 3 attempts which is the maximum number of attempts allowed. Please try again later.")
