# Program 2: Keep doubling game...

def main():
    current_value = int(input("Enter a number: "))
    while current_value < 100:
        current_value = current_value * 2
        print(current_value)

if __name__ == "__main__":
    main()