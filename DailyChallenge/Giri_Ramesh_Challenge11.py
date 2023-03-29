# Create a program to ask the user to enter user name and password and show successful login if both verified.
# In case of incorrect details it must ask the user to enter again for at least 3 times before showing the message of out of attempts.

data = []

while True:
    userName = input("Please create your username:- ")
    password = input("Please create your password:- ")

    if userName == "" or password == "": #checks whether the input is empty or not.
        print("you can not leave input Fields empty")
    else:
        #adds the typed username and password in data list.
        data.append(userName)
        data.append(password)
        counter = 0
        for i in range(3): #loop runs For 3 time iF invalid credentials.
            userNameLogin = input("Enter your username to login:- ")
            passwordLogin = input("Enter your password to login:- ")
            if userNameLogin == "" or passwordLogin == "": #checks whether the input is empty or not.
               print("you can not leave input Fields empty")
            else:
                #iF both value match, logged in successFully.
                if userNameLogin == data[0] and passwordLogin == data[1]: 
                    print("You have logged in successfully")
                    data = [] 
                    break
                else:
                    #otherwise counter will increase by 1.
                    counter += 1
                    print("Invalid username or password, you have used", counter, "attempts out oF 3")
                    
                # if counter == 3: 3 attempts allowed.
                    print("You have used maximum attempt")
                    break
                
            



