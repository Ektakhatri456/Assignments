# Program 6: Double the value until 100.
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    #taking user input
    current_number = float(input("Enter the number: "))
    
    #loop until the number is 100 or greater
    while current_number < 100:
        current_number *= 2
        print("The current number is: ", current_number, end = " ")

if __name__ == "__main__":
    main()
