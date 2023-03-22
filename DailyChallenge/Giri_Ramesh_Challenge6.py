# Write a program that takes a string as input from the user. The program must show the length of the input if the input is a number/digit.
# Else, it must show that the input is not an integer.

string_input = input("Please type something:- ")

isDigit = string_input.isdigit() #it checks that input is digit or not.
if isDigit:
    print("length is:-",len(string_input))
else:
    print("the input is not an integer")