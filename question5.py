address = input("Please enter your full address: ")
distance = float(input("Please enter the distance in KM between your address and the restaurant: "))

# it calculates delivery charge based on distance
if distance > 0 and distance <= 5:
    deliveryCharge = 5
elif distance > 5 and distance <= 10:
    deliveryCharge = 8
elif distance > 10 and distance <= 12:
    deliveryCharge = 10
else:
    print("Delivery cannot be done for distances greater than 12 KM.")
    exit()


print("The delivery charge for the address", address, "located", distance, "KM from the restaurant is $", deliveryCharge)