# Program 5: Printing 10 random numbers (1 - 100)

import random

def main():
    for _ in range(10):
        value = random.randint(1, 100)
        print(value, end = " ")

if __name__ == "__main__":
    main()
