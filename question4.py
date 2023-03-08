totalAmount = float(input("Total amount: $"))
tip = float(input("Tip (In Cents): ")) / 100
paymentByCard = float(input("Total Payment received by Card: $"))
serviceChargeCard = float(input("Service Charge on Payment made by Card (in percentage): ")) / 100
paymentByCash = float(input("Total Payment received in Cash: $"))

# it calculates total received amount
totalReceivedAmount = paymentByCard * (1 - serviceChargeCard) + paymentByCash

#it calculates total due amount
totalDueAmount = totalAmount + tip

#it calculates change that should be returned to customer
change = totalReceivedAmount - totalDueAmount

outstanding = totalDueAmount - totalReceivedAmount


if totalReceivedAmount < totalDueAmount:
    print("Outstanding amount and need to be paid by customer:- $", outstanding)
else:    
    print("Change to be returned to the customer:- $", change)