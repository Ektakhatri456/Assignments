# Program 1: Dice Rolling Simulator

import random

sides = 6
def roll_dice():
    """Simulate rolling a dice."""
    die_1 = random.randint(1, sides)
    die_2 = random.randint(1, sides)
    total = die_1 + die_2
    print(f"Rolling the dice...{die_1} + {die_2} = {total}")
    return total

def main():
    """Main function to run the dice rolling simulator."""

    die_1 = 10 # Placeholder for the first die
    print(f"Initial value for die_1: {die_1}")

    for _ in range(3):
        die_1 = roll_dice()
        print(f"New value for die_1: {die_1}") 

if __name__ == "__main__":
    main()


