#Create a program to ask the user to enter 3 values and print the smaller number among the same.
#Note: no use of lists or other data structure.

num1 = eval(input("Enter num1:- "))
num2 = eval(input("Enter num2:- "))
num3 = eval(input("Enter num3:- "))

if num1 < num2 and num1 < num3:
    print("The Minimum number is:-", num1)
elif num2 < num1 and num2 < num3:
    print("The Minimum number is:-", num2)
else:
    print("The Minimum number is:-", num3)

#we can also use min() Function to determine the minimum number.