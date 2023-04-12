smallest = 999999999

# Asking user to enter 5 values
for i in range(5):
    num = int(input("Enter a number: "))
    if num < smallest:
        smallest = num

# Printing the smallest number entered by user
print("The smallest number is:", smallest)