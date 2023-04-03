# Create a program that ask the user to enter a number, and then ask him to enter the values that many times.
# Once all the values entered the program must show the values in descending order.

desiredNumber = input("Plase enter a number you want to enter except 0 or negative number:- ")
data = []
if desiredNumber == "": #checks whether the input Field is empty or not.
    print("You cannot leave input Field empty.")
elif desiredNumber == '0': #checks whether the value is equal to 0 or not.
    print("You entered", desiredNumber,", so we cannot move Further.")
elif desiredNumber < '0': #checks whether the value is less than 0 or not.
    print("You cannot enter negative number")
else:
    convertedToInt = int(desiredNumber) #converts the value to an integer.
    for i in range(convertedToInt): #runs the loops the times value that user has typed.
        convertedToInt-=1 #decreases the count by 1 everytime loop runs.
        numberOFValues = input(f"please enter numbers {convertedToInt + 1} oF times:- ")
        if numberOFValues == "": #checks whether the input Field is empty or not.
            print("You cannot leave input Field empty.")
        else:
            data.append(int(numberOFValues)) #adds the values in list oF data.
            data.sort(reverse=True) #sorts out in decending order, because reverse is True.
           
    print("Desending Order:-", data)

