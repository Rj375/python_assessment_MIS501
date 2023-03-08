# the list of orders for current week
currentWeekOrders = input("Enter the list of orders total prices for the current week separated by spaces: ")
currentWeekOrders = currentWeekOrders.split()
currentWeekOrders = [float(x) for x in currentWeekOrders]

# the list of orders for previous week
previousWeekOrders = input("Enter the list of orders total prices for the previous week separated by spaces: ")
previousWeekOrders = previousWeekOrders.split()
previousWeekOrders = [float(x) for x in previousWeekOrders]

# it calculates average per person sale for current week
totalNumberOfPersonsVisitedInTheCurrentWeek = len(currentWeekOrders)
totalSaleForCurrentWeek  = sum(currentWeekOrders)
averageSaleCurrentWeek = totalSaleForCurrentWeek  / totalNumberOfPersonsVisitedInTheCurrentWeek

# it calculates average per person sale for previous week
totalNumberOfPersonsVisitedInThePreviousWeek = len(previousWeekOrders)
totalSaleForPreviousWeek = sum(previousWeekOrders)
averageSalePreviousWeek = totalSaleForPreviousWeek / totalNumberOfPersonsVisitedInThePreviousWeek


print("Current Week per person average sale = AUD", averageSaleCurrentWeek)
print("Last Week per person average sale = AUD", averageSalePreviousWeek)