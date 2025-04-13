# Program 4: 
#Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

minimum_height = 70 #height in inches

def main():
    height = float(input("Please tell your height in inches: "))
    if height >= minimum_height:
        print("You are tall enough to ride.")
    else:
        print("You are not tall enough to ride, but maybe next year.")

if __name__ == "__main__":
    main()

