# Create a program that keep asking the user to enter a positive number until he enters 0 to stop.
# Than please print the smallest number out of the number entered by the user.


data = []

while True:
    userInputs = eval(input("Please enter the positive number you want to enter. Enter 0 to stop:- ")) 
    if userInputs >= 0: #it checks iF the user has entered a negative number or not.
        data.append(userInputs) #it adds input value in data list.
        if userInputs == 0: #it checks iF the input value is 0 or not.
            minValue = min(data) #it Finds out the minimum value From the list.
            if len(data) == 1:
                print("The Smallest number From the list is:-",minValue)
                break
            else:
                data.pop() #it removes last input value from data list which is 0.
                print("The Smallest number From the list is:-",minValue)
                break
    else:
        print("you cannot enter a negative number.")