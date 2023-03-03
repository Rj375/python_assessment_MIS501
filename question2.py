
width = float(input("Enter the width of the restaurant in meters: "))
length = float(input("Enter the length of the restaurant in meters: "))


area = width * length # Calculate the area of the restaurant in square meters

people = int(area / 1.2) # Calculate the number of people that can be accommodated in the restaurant

# Output
if people > 60:
   print("A Maximum of 60 persons are allowed.")
else:
   print("The restuarant can accomodate", people, "people")