import random

print("Welcome to your password generator :) ")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURTUVWXYZ!@#$%^&*().,?/\[]0123456789"
number = input("Amount of password generate : ")
number = int(number)
length = input("Your password length : ")
length = int(length)
print("\nhere are your passwords : ")

for password in range(number):
    passwords = ""
    for password in range(length):
        passwords += random.choice(chars)
    print(passwords)