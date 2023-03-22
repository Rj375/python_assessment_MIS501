i = 0 #its a deFInite loop cuz it saying how many times to run loop or it will stop aFter certain repetition?condition meet.
while i <=7: #deFinite loop means it should stop aFter certain condition, or it has condition.
    print("Hello, I am Ramesh Giri")
    i = i + 1

#while true: its a inFInity loop cuz there is no condition.
    #print("hello")

#indeFInite loop is combination oF both deFinite and infinite loop.
#the code may or may not stop.
#it will keep running until speciFIc condition is meet.
j = 1
while j != 0:
    j = eval(input("Please enter integer"))
    if(j == 7):
      print("Hello, you have typed the desired interger.")



# write a program to ask a user to type values 5 times
user_input = 0

while user_input < 5:
   user_input = eval(input("Please enter integer: "))
   user_input = user_input + 1 #or user_input += 1

#or
# for k in range(5):
#     input("type me")


   if user_input < 0: #it will check whether the input is in minus or not. eg:- -1, -2 etc.
       print("it is negative")
   elif user_input > 0:
       print("it is positive")


num = eval(input("please enter the value"))

while num < 20:
    num = num + 1
    if num%10 == 0:
        break
    elif num%5 == 0:
        continue
    print(num)


#For loop, i directly access the value.
name = "python"
k = 0
for k in name:

    print(k)

for k in range(0, len(name), 2): #range(start, length, 2 iteration)
    print(name[k])

# for k in range(0, len(name)):
#     name[k] = eval(input("Num:- "))
# print(name)
for k in range(100):
    print(k+1)

for k in range(5):
   input_value = input("please enter the value")
   print(input_value)
    
print(list(range(1,10)))
print(tuple(range(1,10)))

