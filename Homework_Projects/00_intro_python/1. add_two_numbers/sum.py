#Program 1: Adding two numbers

def main():
    
    print("Hey there! Let's add two numbers together.")

    num_1 : str = int(input("Enter the first number: "))
    num_1 : int = int(num_1)

    num_2 : str = int(input("Enter the second number: "))
    num_2 : int = int(num_2)

    total : int = num_1 + num_2

    print("The sum of two nummbers is: " +str (total) + ".")

if __name__ == "__main__":
    main()

