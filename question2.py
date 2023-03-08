width = float(input("Enter the width of the restaurant in meters: "))
length = float(input("Enter the length of the restaurant in meters: "))

# It calculates the area of the restaurant in square meters
area = width * length 

# It calculates the number of people that can be accommodated in the restaurant
people = int(area / 1.2) 


if people > 60:
   print("A Maximum of 60 persons are allowed.")
else:
   print("The restuarant can accomodate", people, "people")