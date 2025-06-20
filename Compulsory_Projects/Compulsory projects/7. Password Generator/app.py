# Project 7: Password Generator Python Project

import random

print("\n Welcome to the Python Password Generator \n")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+.,"

number_of_characters = input("How many characters would you like in your password? ")
number_of_characters = int(number_of_characters)

length = input("How many passwords would you like to generate?")
length = int(length)

print('\n Here are your passwords: \n')

for password in range(length):
    passwords = ""
    for c in range(number_of_characters):
        passwords += random.choice(characters)
    print(passwords)