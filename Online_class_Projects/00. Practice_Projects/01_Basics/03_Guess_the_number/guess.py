# Program 4: Guess my number game...

import random

def main():
    num_to_guess = random.randint(0, 99)
    guess = int(input("I am guessing a number between 0 and 99...Enter a guess: "))

    while guess != num_to_guess:
        if guess > num_to_guess:
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")

        guess = int(input("Enter a new number: "))

    print(f"Congrats! you guessed the right number. the number was {num_to_guess}")

if __name__ == "__main__":
    main()