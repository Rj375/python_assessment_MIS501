# Create a program to ask the user to enter positive values and 0 to quit.
# Print the sum of all the values entered provided by the values repeatedly entered and -ve will not be considered.
# Example:
# Input
# 2 3 3 2 4 5 4 5 5 -9 0
# Output:
# Total vales entered are 7
# Sum is 25

data = []
while True:
    userInput = eval(input("Please enter positive values (enter 0 to quit):- "))
    
    if userInput == 0: #checks where the userInput is 0 or not, if True,
        add = sum(data) #adds all the input typed by user.
        print("Total vales entered are", len(data)) #checks length of the data list.
        print("the sum of the user input is", add) 
        exit() #exits the program.
    elif userInput < 0: #checks where the userInput is less than 0 or not, if True,
        print("Negative number is not accepted")
        continue #skips the numbers which are less than 0 or negative.
        # or we can do data.pop()
    else:
        data.append(userInput) #add all the inputs in data list.


