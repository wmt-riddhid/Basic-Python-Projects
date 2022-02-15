# This is guess the number game (computer)

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 5
    while guess != random_number :
        guess = int(input("Guess a number between 1 and 10 : "))
        if guess < random_number:
            print("Sorry, Guess again, Too low")
        elif guess > random_number :
            print("Sorry, Guess again, Too high")
    
    print("YaaYYY...Congratulations !!! You have guessed the number correct")

guess(10)