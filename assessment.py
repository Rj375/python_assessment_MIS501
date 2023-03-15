
#Question 1
name = input("Enter your Name:- ")
phone = input("Enter your Phone Number:- ")
birthYear = int(input("Enter your Birth Year(yyyy):- ")) #year is being converted to interger here itself.
currentCity = input("Enter your Current City:- ")
email = input("Enter your Email Address:- ")

# it calculates the age of the user.
age = 2023 - birthYear 

#it checks where the user is 21 years old.
if age > 21: 
    print("The name is:-", name)
    print("The phone is:-", phone)
    print("The age is:-", age)
    print("The current city is:-", currentCity)
    print("The email is:-", email)
else:
    print("Customer has to be above 21 years old to view the information")    
 


#Question 2
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



#Question 3
# the list of orders for current week
currentWeekOrders = input("Enter the list of orders total prices for the current week separated by spaces: ")
currentWeekOrders = currentWeekOrders.split() #it splits string input into a list/array oF characters.

for currentWeek in currentWeekOrders: #loops through the input that user entered
   convertCurrentWeekIntoFloat = float(currentWeek) #converts the currentWeek into a float
   currentWeekOrders = [convertCurrentWeekIntoFloat] #assigns converted input in list/array.

# the list of orders for previous week
previousWeekOrders = input("Enter the list of orders total prices for the previous week separated by spaces: ")
previousWeekOrders = previousWeekOrders.split() #it splits string input into a list/array oF characters.

for previousWeek in previousWeekOrders: #loops through the input that user entered
   convertPreviousWeekIntoFloat = float(previousWeek) #converts the previousWeek into a float
   previousWeekOrders = [convertPreviousWeekIntoFloat] #assigns converted input in list/array.

# it calculates average per person sale for current week
totalNumberOfPersonsVisitedInTheCurrentWeek = len(currentWeekOrders) #checks the length
totalSaleForCurrentWeek  = sum(currentWeekOrders) #adds all the inputs
averageSaleCurrentWeek = totalSaleForCurrentWeek  / totalNumberOfPersonsVisitedInTheCurrentWeek

# it calculates average per person sale for previous week
totalNumberOfPersonsVisitedInThePreviousWeek = len(previousWeekOrders) #checks the length
totalSaleForPreviousWeek = sum(previousWeekOrders) #adds all the inputs
averageSalePreviousWeek = totalSaleForPreviousWeek / totalNumberOfPersonsVisitedInThePreviousWeek


print("Current Week per person average sale = AUD", averageSaleCurrentWeek)
print("Last Week per person average sale = AUD", averageSalePreviousWeek)




#Question 4

totalAmount = float(input("Total amount: $"))
tip = float(input("Tip (In Cents): ")) / 100
paymentByCard = float(input("Total Payment received by Card: $"))
serviceChargeCard = float(input("Service Charge on Payment made by Card (in percentage): ")) / 100
paymentByCash = float(input("Total Payment received in Cash: $"))

# it calculates total received amount
totalReceivedAmount = paymentByCard * (1 - serviceChargeCard) + paymentByCash

#it calculates total due amount
totalDueAmount = totalAmount + tip

#it calculates change that should be returned to customer
change = totalReceivedAmount - totalDueAmount

outstanding = totalDueAmount - totalReceivedAmount


if totalReceivedAmount < totalDueAmount: #checks whether totalReceivedAmount is less than totalDueAmount.
    print("Outstanding amount and need to be paid by customer:- $", outstanding)
else:    
    print("Change to be returned to the customer:- $", change)
    



#Question 5
address = input("Please enter your full address: ")
distance = float(input("Please enter the distance in KM between your address and the restaurant: "))

# it checks delivery charge based on distance using comparative operators.
if distance > 0 and distance <= 5:
    deliveryCharge = 5
elif distance > 5 and distance <= 10:
    deliveryCharge = 8
elif distance > 10 and distance <= 12:
    deliveryCharge = 10
else:
    print("Delivery cannot be done for distances greater than 12 KM.")
    


print("The delivery charge for the address", address, "located", distance, "KM from the restaurant is $", deliveryCharge)





#Question 6
orderCost = float(input("Order base cost: AUD" ))
orderType = int(input("Order type (1 for dine in, 2 for pick up, 3 for delivery): "))

# it calculates charges based on order type
# dineInOrderType = 1,
# pickupOrderType = 2,
# deliveryOrderType = 3
if orderType == 1: # it checks orderType and charges according to that using comparative operators.
    totalCharges = orderCost * 1.08
elif orderType == 2:
    totalCharges = orderCost
elif orderType == 3:
    totalCharges = orderCost * 1.1
else:
    print("Invalid order type. Please enter 1, 2, or 3.")
    


print("Total charges: AUD", totalCharges)





#Question 7
temperature = float(input("Enter the temperature value: "))
conversionForm = int(input("Enter the conversion form (1 for Centigrade to Fahrenheit, 2 for Fahrenheit to Centigrade): "))

# it converts the temperature
if conversionForm == 1:
    # From Centigrade to Fahrenheit
    temperatureConverted = (9/5) * temperature + 32
    print(temperature, "Centigrade =", temperatureConverted, "Fahrenheit")
elif conversionForm == 2:
    # From Fahrenheit to Centigrade
    temperatureConverted = (5/9) * (temperature - 32)
    print(temperature, "Fahrenheit =", temperatureConverted, "Centigrade")
else:
    print("Invalid entry.")
    
    





#Question 8
position = str.lower(input("Enter the position of the employee (chef, waiter, or delivery): "))
hoursWorked = float(input("Enter the number of monthly hours worked: "))


# checks the position that user has entered.
if position == "chef":
    payRate = 50
elif position == "waiter":
    payRate = 40
elif position == "deliver":
    payRate = 35
else:
    print("Invalid position.")
    exit() #with this aFter calculation is done the execution ends iF it prints Invalid position.

grossIncome = payRate * hoursWorked

# it calculates the income aFter 20% tax 
taxRate = 0.2
taxAmount = grossIncome * taxRate
netIncome = grossIncome - taxAmount


print("The net monthly income of the employee is:", netIncome)








#Question 9
mobilePhone = input("Insert your phone number")
password = input("Enter your password")


#it checks where the mobilePhone has exactly 10 digits and where the length oF password is greater than or equal to 8.
if len(mobilePhone) == 10 and len(password) >= 8:
    print("Valid Credentials")
else:
    print("Invalid Credentials")
