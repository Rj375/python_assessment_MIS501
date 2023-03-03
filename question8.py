
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
