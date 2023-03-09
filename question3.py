# the list of orders for current week
currentWeekOrders = input("Enter the list of orders total prices for the current week separated by spaces: ")
currentWeekOrders = currentWeekOrders.split() #it splits string input into a list/array oF characters.

# currentWeekOrders = [float(x) for x in currentWeekOrders]

for currentWeek in currentWeekOrders: #loops through the input that user entered
   convertCurrentWeekIntoFloat = float(currentWeek) #converts the currentWeek into a float
   currentWeekOrders = [convertCurrentWeekIntoFloat] #assigns converted input in list/array.

# the list of orders for previous week
previousWeekOrders = input("Enter the list of orders total prices for the previous week separated by spaces: ")
previousWeekOrders = previousWeekOrders.split() #it splits string input into a list/array oF characters.

# previousWeekOrders = [float(x) for x in previousWeekOrders]

for previousWeek in previousWeekOrders: #loops through the input that user entered
   convertPreviousWeekIntoFloat = float(previousWeek) #converts the previousWeek into a float
   previousWeekOrders = [convertPreviousWeekIntoFloat] #assigns converted input in list/array.

# it calculates average per person sale for current week
totalNumberOfPersonsVisitedInTheCurrentWeek = len(currentWeekOrders) #checks the length
totalSaleForCurrentWeek  = sum(currentWeekOrders) #adds all the inputs
averageSaleCurrentWeek = totalSaleForCurrentWeek  / totalNumberOfPersonsVisitedInTheCurrentWeek

# it calculates average per person sale for previous week
totalNumberOfPersonsVisitedInThePreviousWeek = len(previousWeekOrders) #checks the length
totalSaleForPreviousWeek = sum(previousWeekOrders) #adds all the inputs
averageSalePreviousWeek = totalSaleForPreviousWeek / totalNumberOfPersonsVisitedInThePreviousWeek


print("Current Week per person average sale = AUD", averageSaleCurrentWeek)
print("Last Week per person average sale = AUD", averageSalePreviousWeek)