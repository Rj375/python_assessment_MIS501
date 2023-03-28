# Create a program  to print the counting from 1 to 20 skipping the values that can be devided by 4.
# Note: use Continue (edited) 

counterStart = 1
counterEnd = 20

for counter in range(counterStart, counterEnd):
    if counter % 4 == 0: #checks whether the number is divisible by 4 or not.
        continue # iF divisible by 4, then it skips that number.
    else:
        print(counter)
