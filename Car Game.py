print("Welcome to the Car Game! ")
start = False
while True:
    Userinput = input("Type: ").lower()
    if Userinput == "help":
        print('''start - Start the car
stop - Stop the car
quit - Quit the Game''')
    elif Userinput == "start":
        if start == True:
            print("The car has already been started.")
        else:
            print("The car has started! Vroom!! ")
            start = True
    elif Userinput == "stop":
        if start != True:
            print("The car has already been stopped.")
        else:
            print("The car has stopped! ")
            start = False
    elif Userinput == "quit":
        print("You ended the game! Thank you!")
        Previous_Choice = Userinput
        break
    else:
        print("I'm sorry I didn't understand that..")
#I think this is fine