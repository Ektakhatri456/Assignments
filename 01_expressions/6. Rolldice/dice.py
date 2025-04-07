#Program 6: Rolling Dice 

import random

def main():

    # Roll the dice
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    
    # Display the results
    print(f"Rolling the dice...")
    print(f"Die 1: {die_1}")
    print(f"Die 2: {die_2}")
    

    # Calculate the total of the two dice
    total = die_1 + die_2

    # Display the total
    print("The total is", total)



if __name__ == "__main__":
    main()
