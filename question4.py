
total_amount = float(input("Total amount: $"))
tip = float(input("Tip (In Cents): ")) / 100
payment_by_card = float(input("Total Payment received by Card: $"))
service_charge_card = float(input("Service Charge on Payment made by Card (in percentage): ")) / 100
payment_by_cash = float(input("Total Payment received in Cash: $"))

# it calculates total received amount
total_received_amount = payment_by_card * (1 - service_charge_card) + payment_by_cash

#it calculates total due amount
total_due_amount = total_amount + tip

#it calculates change that should be returned to customer
change = total_received_amount - total_due_amount

outstanding = total_due_amount - total_received_amount


if total_received_amount < total_due_amount:
    print("Outstanding amount and need to be paid by customer:- $", outstanding)
else:    
    print("Change to be returned to the customer:- $", change)