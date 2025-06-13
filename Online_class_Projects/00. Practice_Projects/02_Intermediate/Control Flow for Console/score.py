# Program 1: High - Low Game

import random

NUM_ROUNDS = 5
score = 0

def play_round(round_number):
    global score
    print(f"Round {round_number}")

    #step 1: generating random numbers for player and computer

    user_number = random.randint(1, 100)
    comp_number = random.randint(1, 100)

    #  Show player's number (not computer's number)
    print(f"Your number is {user_number}")


    #step 2: asking the player to guess

    guess = input("Do you think your number is higher or lower than the computer's? ")

    #Extension 1: Safeguard user's input
    while guess.lower() not in ["higher", "lower"]:
        print("Please enter either 'higher' or 'lower': ")
        guess = input("Do you think your number is higher or lower than the computer's? ")

    #step 3: Comparing the score    

    if (guess == "higher" and user_number > comp_number) or (guess == "lower" and user_number < comp_number):
        print("You guessed correctly!")
        score += 1

    else:
        print(f"Aww, that's incorrect. The computer's number was {comp_number}.")
    print(f"You score is now {score} \n")


def play_game():
    print("Welcome to the High-Low Game!")
    print("------------------------------")

    #step 4: Play muliple rounds

    for round_number in range(1, NUM_ROUNDS + 1):
        play_round(round_number)

    #step 5: End of game feedback based on score
    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("WOW! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, You played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()








