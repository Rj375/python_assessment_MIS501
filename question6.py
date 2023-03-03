# Prompt user for inputs
order_cost = float(input("Order base cost: AUD" ))
order_type = int(input("Order type (1 for dine in, 2 for pick up, 3 for delivery): "))

# Calculate total charges based on order type
# dine_in_order_type = 1,
# pickup_order_type = 2,
# delivery_order_type = 3
if order_type == 1:
    total_charges = order_cost * 1.08
elif order_type == 2:
    total_charges = order_cost
elif order_type == 3:
    total_charges = order_cost * 1.1
else:
    print("Invalid order type. Please enter 1, 2, or 3.")
    exit()

# Output result
print("Total charges: AUD {:.2f}".format(total_charges))