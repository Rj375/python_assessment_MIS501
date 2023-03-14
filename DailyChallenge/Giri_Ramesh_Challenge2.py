#Write a program to ask the user to enter his name and year of birth and print a greeting message with his name and age.
name_oF_user = input("Please Enter Your Full Name:- ")
user_year_OF_birth = int(input("Please Enter your Year oF Birth:- "))

#it calculates the age oF user.
age_oF_user = 2023 - user_year_OF_birth

print("Hi", name_oF_user, ",your age is", age_oF_user)