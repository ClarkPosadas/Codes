Guess_count = 0
Secret_Number = 9

while Guess_count < 3:
    Guess = int(input("Guess: "))
    Guess_count += 1
    if Guess == Secret_Number:
        print("You win!")
        break
else:
    print("You lose!")
#Learning Python test