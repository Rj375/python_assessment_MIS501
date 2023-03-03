# Prompt user for list of orders total prices for current week
current_week_orders = input("Enter the list of orders total prices for the current week separated by spaces: ")
current_week_orders = current_week_orders.split()
current_week_orders = [float(x) for x in current_week_orders]

# Prompt user for list of orders total prices for previous week
previous_week_orders = input("Enter the list of orders total prices for the previous week separated by spaces: ")
previous_week_orders = previous_week_orders.split()
previous_week_orders = [float(x) for x in previous_week_orders]

# Calculate average per person sale for current week
total_number_of_persons_visited_in_the_current_Week = len(current_week_orders)
total_sale_for_current_week  = sum(current_week_orders)
average_sale_current_week = total_sale_for_current_week  / total_number_of_persons_visited_in_the_current_Week

# Calculate average per person sale for previous week
total_number_of_persons_visited_in_the_previous_Week = len(previous_week_orders)
total_sale_for_previous_week = sum(previous_week_orders)
average_sale_previous_week = total_sale_for_previous_week / total_number_of_persons_visited_in_the_previous_Week

# Output results
print("Current Week per person average sale = AUD {:.2f}".format(average_sale_current_week))
print("Last Week per person average sale = AUD {:.2f}".format(average_sale_previous_week))