while True:
    first_number = float(input("Enter Your First Number: "))
    second_number = float(input("Enter Your Second Number: "))

    while True:
        operator = input("Please enter your operator (+/-/*/%/Exit): ")

        if operator == "+":
            result = first_number + second_number
            message = f"Your result in addition is:  {result:g}"
        elif operator == "-":
            result = first_number - second_number
            message = f"Your result in subtraction is:  {result:g}"
        elif operator == "*":
            result = first_number * second_number
            message = f"Your result in multiplication is:  {result:g}"
        elif operator == "/":
            result = first_number / second_number
            message = f"Your result in division is:  {result:g}"
        elif operator == "%":
            result = first_number % second_number
            message = f"Your result in modulus is:  {result:g}"
        elif operator.upper() == "EXIT":
            break
        else:
            message = "Please enter a proper operator: "
        print(message)
