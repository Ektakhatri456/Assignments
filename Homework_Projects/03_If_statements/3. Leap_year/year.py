# Program 3: Leap year
#Write a program that reads a year from the user and tells whether a given year is a leap year or not.

def main():
    year = int(input("Please enter a year: "))

    if year % 4 == 0:
        print("The year is a leap year.")

    elif year % 100 == 0:
        print("The year is a leap year.")

    elif year % 400 == 0:
        print("The year is a leap year.")

    else:
        print("The year is not a leap year.")

if __name__ == "__main__":
    main()
    