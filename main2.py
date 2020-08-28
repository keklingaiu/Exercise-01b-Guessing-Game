import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

number = random.randrange(1,10)
turns = 0
try:
    while turns < 3:
        guess = int(input("Guess a number from 1 to 10: "))

        if guess == number:
            print("Great job! You got it!")
            break
        elif guess > number:
            print("Your number was a little high! Guess again!")
        else:
            print("Your number was a little low! Guess again!")
        turns += 1
    if not turns < 3:
        print("Sorry, better luck next time.")
        print("The number was " + str(number))
except:
    print("The value you entered is not accepted.")