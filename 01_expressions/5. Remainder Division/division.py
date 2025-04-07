# Program 5: Remainder division
# This program performs integer division and returns the quotient and remainder.

#Ask the user for two numbers, one at a time, 
#and then print the result of dividing the first number by the second and also the remainder of the division.


def main():
    num_1 = int(input("Enter the first number (Dividend): "))
    num_2 = int(input("Enter the second number (Divisor): "))

    quotient = num_1 / num_2
    remainder = num_1 % num_2

    print(f"The quotient of {num_1} and {num_2} is {quotient:.2f} along with the remainder {remainder}.")

if __name__ == "__main__":
    main()