position = input("Enter the position of the employee (chef, waiter, or delivery): ")
hoursWorked = float(input("Enter the number of monthly hours worked: "))

# checks the position that user has entered.
if position == "chef":
    payRate = 50
elif position == "waiter":
    payRate = 40
elif position == "delivery":
    payRate = 35
else:
    print("Invalid position.")
    exit()

grossIncome = payRate * hoursWorked

# it calculates the income aFter 20% tax 
taxRate = 0.2
taxAmount = grossIncome * taxRate
netIncome = grossIncome - taxAmount


print("The net monthly income of the employee is:", netIncome)
