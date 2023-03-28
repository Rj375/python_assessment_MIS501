# Create a Program to ask the user to enter multiple values until he enter a Negative value, and print how many unique numbers entered

data = []
while True:
    givenValue = eval(input("Please enter any number (Enter negative number to stop):- "))
    if givenValue < 0: #iF value is less than 0,
        uniqueData = set(data) # then here it is a set which Filters the unique value.
        print("You have entered", len(uniqueData) ,"unique numbers excluding the negative value")
        break
    else:
        data.append(givenValue) # here it adds values to the list oF data.
        