i = 0

if i < 5:
    print("hello")
else:
    pass

# or

if i == 0:
    pass
elif i == 1:
    pass
elif i == 2:
    pass
elif i == 3:
    print("Hello")

#nested loops:-
data = []
for i in range(3):
    for counter in range(1,4):
        userInput = eval(input(f"Please enter assignment {counter} marks"))
        # userInput = eval(input("Please enter assignment", str(counter) ,"marks"))
        if userInput == "":
            print("you can't leave inputs empty")
        else:
            data.append(userInput)
print(data)

li = ['hello', 'hello123']
amtli = [2,4,6,8]
name1 = ['A', 'B', 'C', 'D', 'E', 'F']

userName = 'ramesh'
password = '123'

# for i in range(len(li)):
#     if userName == li[i] and password == amtli[i]:
#         print("successFully signed in")

if li.count(userName) == 0:
    print('no record')
else:
    n = li.index(userName)
    if userName == li[n] and password == amtli[n]:
        print('successFully signed in')
    else:
        print('wrong')
