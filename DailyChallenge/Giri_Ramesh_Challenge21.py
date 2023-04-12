# Create a program to ask the user to enter 5 values and print the smallest among them.
# Note: Please solve this exercise without using Min Max and list or any data structure.
# A simple implication of loops and conditions are required.


smallNumber = 10000000000000000

def findSmallestNumber(i): #here i is taken as parameter.
    global smallNumber #make variable global to the Function
    userInputNumber = eval(input(f"Enter a number 5 times, this is your {i+1} time:- "))
    if userInputNumber < smallNumber: #check whether the number typed is smallest or not.
        smallNumber = userInputNumber #iF smallest then it will assign that value to smallNumber.


for i in range(5):
    findSmallestNumber(i) #Function is called inside the loop. where, i is passed as a argument.

print("The smallest number among them is:", smallNumber)
