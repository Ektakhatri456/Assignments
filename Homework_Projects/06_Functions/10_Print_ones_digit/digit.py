# Program 10: Prints the One's digit in the value

# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2

def prints_ones_digit(num):
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))

    prints_ones_digit(num)

if __name__ == "__main__":
    main()