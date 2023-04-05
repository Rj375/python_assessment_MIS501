import re

# name = "ramesh"

# caseFold = "ß"

# print(name.capitalize())
# print(caseFold.casefold()) 
# print(name.isalpha())
# print(name.isnumeric())
# print(name.isalnum())
# print(name.isupper())
# print(name.islower())
# print(name.lower())
# print(name.upper())
# print(name.title())

# randomString = "Python is Versatile is Language"
# subString = "is"
# num = randomString.count(subString)
# print(num)
# location = randomString.find("is")
# print(location)
# print(randomString.startswith("python is"))
# print(randomString.endswith("age"))
# print(randomString.swapcase())
# print(randomString.replace("is", "very"))

# newString = input("enter string")


# dob = "25/07/1996"
# list = dob.split('/')
# print(list)

# # string.Format()

# regex = r"\d{4}"
# testStr = "023tutuytuy"

# match = re.match(regex, testStr)

# if match:
#     print("match found")
# else:
#     print("no match found")

userInput = input("Please enter your name:- ")

isSpace = userInput.count(" ") #checks whether the user has name with space or not.

if isSpace == 1:
    splittedValue = userInput.split()
    print(splittedValue[0], splittedValue[1])
else:
    print("Please enter Full name with spaces")

# splittedValue = userInput.split()


# if len(splittedValue) >= 2:
#     print(splittedValue[0], splittedValue[1])
# else:
#     print("Please enter Full name")

# emailRegex = re.compile(r"^[a-zA-Z@]{5,20}")

# userInput = input("enter email:- ")

# isValid = re.search(emailRegex, userInput)

# if isValid != True:
#     print("No")
# else:
#     print("Good")