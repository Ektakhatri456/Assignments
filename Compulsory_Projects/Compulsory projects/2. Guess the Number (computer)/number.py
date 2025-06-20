# Project 2: Guess the number (computer)

import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:    # we will use loop here for till we get the right answer.
            guess = int(input(f"Guess any number between 1 and {x}: "))
            if guess < random_number:
                  print("Too low. Guess again.")
            elif guess > random_number:
                  print("Too high. Guess again.")

    print(f"🎉Congrats, you have guessed the right number {random_number}.")

guess(10)
    