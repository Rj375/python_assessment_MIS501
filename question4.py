
total_amount = float(input("Total amount: $"))
tip = float(input("Tip (In Cents): ")) / 100
payment_by_card = float(input("Total Payment received by Card: $"))
service_charge_card = float(input("Service Charge on Payment made by Card (in percentage): ")) / 100
payment_by_cash = float(input("Total Payment received in Cash: $"))

# Calculate total amount received
total_received_amount = payment_by_card * (1 - service_charge_card) + payment_by_cash

# Calculate total amount due (invoice amount + tip)
total_due_amount = total_amount + tip

# Calculate change to be returned to the customer
change = total_received_amount - total_due_amount

outstanding = total_due_amount - total_received_amount

# Output result
if total_received_amount < total_due_amount:
    print("Outstanding amount and need to be paid by customer:- ${:.2f}".format(outstanding))
else:    
    print("Change to be returned to the customer:- ${:.2f}".format(change))