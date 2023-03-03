import datetime

# simple way.
age1 = input("enter the age")

int1 = int(age1)
print(2023 - int1)


#with Function.
def calculate_year(user_age):
    today = 2023
    age_int = int(user_age)
    year = today - age_int
    return year

user_age = input("enter the age") #or 
# birth_date = int(input("enter the age"))
year = calculate_year(user_age)
print(f"The user's year oF birth is {year}")


# another way.
age2 = int(input("Enter your age: "))
current_year = datetime.datetime.now().year # Get the current year
birth_year = current_year - age2 # Calculate the birth year
print("Your birth year is:", birth_year)