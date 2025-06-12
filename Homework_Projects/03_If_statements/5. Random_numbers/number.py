# Program 5: Random numbers 
# Print 10 random numbers in the range 1 to 100.

import random

range_of_numbers = 10
minimum_value : int = 1
maximum_value : int = 100

def main():
    for i in range(range_of_numbers):
        print(random.randint(minimum_value, maximum_value),end = " ")
if __name__ == "__main__":
    main()

