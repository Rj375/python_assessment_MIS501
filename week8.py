# def hello(a,b):
#     print(a,b)

# hello("Hello", "world!")

# def name(fname, lname="Giri"):
#     print(fname, lname)

# name("Giri", "Ramesh")
# name(lname="Giri", fname="Ramesh")

# def add():
#     num1 = 5
#     num2 = 5
#     return num1 + num2

# total = add()

# print(total + 5)

# def add1():
#     num1 = 5
#     num2 = 5
#     return num1, num2

# a,b= add1()

# print(a+b+5)

# def ask():
#     fname=input("Please enter your fname")
#     lname=input("Please enter your lname")
#     return fname, lname

# def askyob():
#     yob = eval(input("Please enter your yob"))
#     return yob

# def age():
#     print("age is", 2023-askyob())

# def display():
#     fname, lname=ask()
#     print("Hi", fname, lname)

# display()


# def askUser():
#     global firstName #need to write global cuz variable is not accessible which is inside the function.
#     global lastName  #need to write global cuz variable is not accessible which is inside the function.
#     firstName = input("First Name")
#     lastName = input("Last Name")
#     return firstName, lastName
# askUser()
# print(firstName, lastName) #need to write global cuz variable is not accessible which is inside the function.

i=7
def incre():
    global i #need to write global cuz variable is not accessible which is inside the function.
    i=i+7

incre()
print(i) #need to write global cuz variable is not accessible which is inside the function.

