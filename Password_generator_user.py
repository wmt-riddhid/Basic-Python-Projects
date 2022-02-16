import random
import string

print("WELCOME TO YOUR PASSWORD GENERATOR :) ")
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_chars = list("!@#$%^&*?/()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*?/()")

def random_password_generator():
    length = int(input("Please enter your password length : "))
    alphabets_type = int(input("Please enter the alphabets of your choice : "))
    digits_type = int(input("Please enter the digit of your choice : "))
    special_chars_type = int(input("Please enter the sspecial_chars of your choice : "))
    
    characters_count = alphabets_type + (digits_type) + special_chars_type
    if characters_count > length:
        print("Sorry ! The characters length is greater than length")
        return
    password = ""
    for password in range(alphabets_type):
        password.append(random.choice(alphabets_type))
    for password in range(digits_type):
        password.append(random.choice(digits_type))
    for password in range(special_chars_type):
        password.append(random.choice(special_chars_type))
    if characters_count < length:
        random.shuffle(characters)
        for password in range(length - characters_count):
            password.append(random.choice(characters))
        random.shuffle(password)
        print(password)
random_password_generator()    