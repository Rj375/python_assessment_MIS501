
#Question 1
name = input("Enter your Name:- ")
phone = input("Enter your Phone Number:- ")
birth_year = int(input("Enter your Birth Year:- ")) #year is being converted to interger here itself.
current_city = input("Enter your Current City:- ")
email = input("Enter your Email Address:- ")

age = 2023 - birth_year # it calculates the age of the user.

if age > 21:
    print("The name is:-", name)
    print("The phone is:-", phone)
    print("The age is:-", age)
    print("The current city is:-", current_city)
    print("The email is:-", email)
else:
    print("Customer has to be above 21 years old to view the information")    



#Question 2
width = float(input("Enter the width of the restaurant in meters: "))
length = float(input("Enter the length of the restaurant in meters: "))


area = width * length # Calculate the area of the restaurant in square meters

people = int(area / 1.2) # Calculate the number of people that can be accommodated in the restaurant

# Output
if people > 60:
   print("A Maximum of 60 persons are allowed.")
else:
   print("The restuarant can accomodate", people, "people")