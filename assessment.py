
#Question 1
name = input("Enter your Name:- ")
phone = input("Enter your Phone Number:- ")
birth_year = int(input("Enter your Birth Year:- ")) #year is being converted to interger here itself.
current_city = input("Enter your Current City:- ")
email = input("Enter your Email Address:- ")

# it calculates the age of the user.
age = 2023 - birth_year 

#it checks where the user is 21 years old.
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
current_week_orders = input("Enter the list of orders total prices for the current week separated by spaces: ")
current_week_orders = current_week_orders.split()
current_week_orders = [float(x) for x in current_week_orders]

# the list of orders for previous week
previous_week_orders = input("Enter the list of orders total prices for the previous week separated by spaces: ")
previous_week_orders = previous_week_orders.split()
previous_week_orders = [float(x) for x in previous_week_orders]

# it calculates average per person sale for current week
total_number_of_persons_visited_in_the_current_Week = len(current_week_orders)
total_sale_for_current_week  = sum(current_week_orders)
average_sale_current_week = total_sale_for_current_week  / total_number_of_persons_visited_in_the_current_Week

# it calculates average per person sale for previous week
total_number_of_persons_visited_in_the_previous_Week = len(previous_week_orders)
total_sale_for_previous_week = sum(previous_week_orders)
average_sale_previous_week = total_sale_for_previous_week / total_number_of_persons_visited_in_the_previous_Week


print("Current Week per person average sale = AUD", average_sale_current_week)
print("Last Week per person average sale = AUD", average_sale_previous_week)




#Question 4

total_amount = float(input("Total amount: $"))
tip = float(input("Tip (In Cents): ")) / 100
payment_by_card = float(input("Total Payment received by Card: $"))
service_charge_card = float(input("Service Charge on Payment made by Card (in percentage): ")) / 100
payment_by_cash = float(input("Total Payment received in Cash: $"))

# it calculates total received amount
total_received_amount = payment_by_card * (1 - service_charge_card) + payment_by_cash

#it calculates total due amount
total_due_amount = total_amount + tip

#it calculates change that should be returned to customer
change = total_received_amount - total_due_amount

outstanding = total_due_amount - total_received_amount


if total_received_amount < total_due_amount:
    print("Outstanding amount and need to be paid by customer:- $", outstanding)
else:    
    print("Change to be returned to the customer:- $", change)




#Question 5
address = input("Please enter your full address: ")
distance = float(input("Please enter the distance in KM between your address and the restaurant: "))

# it calculates delivery charge based on distance
if distance > 0 and distance <= 5:
    delivery_charge = 5
elif distance > 5 and distance <= 10:
    delivery_charge = 8
elif distance > 10 and distance <= 12:
    delivery_charge = 10
else:
    print("Delivery cannot be done for distances greater than 12 KM.")
    exit()


print("The delivery charge for the address", address, "located", distance, "KM from the restaurant is $", delivery_charge)





#Question 6
order_cost = float(input("Order base cost: AUD" ))
order_type = int(input("Order type (1 for dine in, 2 for pick up, 3 for delivery): "))

# it calculates charges based on order type
# dine_in_order_type = 1,
# pickup_order_type = 2,
# delivery_order_type = 3
if order_type == 1:
    total_charges = order_cost * 1.08
elif order_type == 2:
    total_charges = order_cost
elif order_type == 3:
    total_charges = order_cost * 1.1
else:
    print("Invalid order type. Please enter 1, 2, or 3.")
    exit()


print("Total charges: AUD", total_charges)





#Question 7
temperature = float(input("Enter the temperature value: "))
conversion_form = int(input("Enter the conversion form (1 for Centigrade to Fahrenheit, 2 for Fahrenheit to Centigrade): "))

# it converts the temperature
if conversion_form == 1:
    # From Centigrade to Fahrenheit
    temperature_converted = (9/5) * temperature + 32
    print(temperature, "Centigrade =", temperature_converted, "Fahrenheit")
elif conversion_form == 2:
    # From Fahrenheit to Centigrade
    temperature_converted = (5/9) * (temperature - 32)
    print(temperature, "Fahrenheit =", temperature_converted, "Centigrade")
else:
    print("Invalid entry.")






#Question 8
position = input("Enter the position of the employee (chef, waiter, or delivery): ")
hours_worked = float(input("Enter the number of monthly hours worked: "))


if position.lower() == "chef":
    pay_rate = 50
elif position.lower() == "waiter":
    pay_rate = 40
elif position.lower() == "delivery":
    pay_rate = 35
else:
    print("Invalid position.")
    exit()

gross_income = pay_rate * hours_worked

# it calculates the income aFter 20% tax 
tax_rate = 0.2
tax_amount = gross_income * tax_rate
net_income = gross_income - tax_amount


print("The net monthly income of the employee is:", net_income)







#Question 9
mobile_phone = input("Insert your phone number")
password = input("Enter your password")


#it checks where the mobile_phone has exactly 10 digits and where the length oF password is greater than or equal to 8.
if len(mobile_phone) == 10 and len(password) >= 8:
    print("Valid Credentials")
else:
    print("Invalid Credentials")
