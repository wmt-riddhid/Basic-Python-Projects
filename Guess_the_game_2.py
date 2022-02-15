# This is a guess the number game (user)

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" :
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low
        feedback = input("It's " + str(guess) + " is too low (L), It is too high (H), It is correct (C) ? ").lower()
        if feedback == "h" :
            high = guess - 2
        elif feedback == "l" :
            low = guess + 2
    print("Yayyyyyy !!!!! Congrulations...the computer guessed your number , " + str(guess) + " , correctly")

computer_guess(10)