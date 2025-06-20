# Project 3: Guess the number (user)

import random
def guess_comp(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H) or too low (L) or correct (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        if low > high:
            print("Something went wrong! The range is invalid. Please restart the game.")
            return  # Exits the function to avoid an infinite loop

    print(f"Congrats! the computer guessed the correct number {guess}.")

guess_comp(2000)