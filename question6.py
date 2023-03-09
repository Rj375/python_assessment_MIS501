orderCost = float(input("Order base cost: AUD" ))
orderType = int(input("Order type (1 for dine in, 2 for pick up, 3 for delivery): "))

# it calculates charges based on order type
# dineInOrderType = 1,
# pickupOrderType = 2,
# deliveryOrderType = 3
if orderType == 1: # it checks orderType and charges according to that using comparative operators.
    totalCharges = orderCost * 1.08
elif orderType == 2:
    totalCharges = orderCost
elif orderType == 3:
    totalCharges = orderCost * 1.1
else:
    print("Invalid order type. Please enter 1, 2, or 3.")
    exit() #with this aFter calculation is done the execution ends iF it prints Invalid position.


print("Total charges: AUD", totalCharges)