import Functions

mydb = Functions.connect()
while True:
    Command = input("Are you an Admin?: (y/n) {x to exit}").lower()
    if Command == "y":
        while True:
            print("\nCRUD SYSTEM ADMIN VIEW")
            print("1 - Add Record")
            print("2 - Update Record")
            print("3 - Delete Record")
            print("4 - View Record")
            print("5 - Exit")
            try:
                Command = int(input("Enter your input: "))
                if Command == 1:
                    Functions.addrecords(mydb)
                elif Command == 2:
                    Functions.updaterecords(mydb)
                elif Command == 3:
                    Functions.deleterecords(mydb)
                elif Command == 4:
                    Functions.viewrecords(mydb)
                elif Command == 5:
                    break
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")
    elif Command == "n":
        while True:
            print("\nCRUD SYSTEM USER VIEW")
            print("1 - View Record")
            print("2 - Exit")

            try:
                Command = int(input("Enter your input: "))
                if Command == 1:
                    Functions.viewrecords(mydb)
                elif Command == 2:
                    break
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")
    elif Command == "x":
        break
    else:
        print("Invalid input")
#e\testss