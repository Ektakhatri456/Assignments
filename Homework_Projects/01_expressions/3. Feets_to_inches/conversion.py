#Program 3: Conversion of feets into inches

def feet_to_inches(feet):
    return feet * 12
def main():
    while True:
        user_input = input("Enter the number of feet (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program...")
            break
        try:
            feet = float(user_input)
            inches = feet_to_inches(feet)
            print(f"{feet} feet is equal to {inches} inches.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()