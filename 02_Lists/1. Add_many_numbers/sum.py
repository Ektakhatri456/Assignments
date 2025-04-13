# Program 1: Addition of many numbers
# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_number(numbers) -> int:
    """
    This function takes a list of numbers and returns the sum of those numbers.

    """
    total : int = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers : list[int]= [2, 4, 6, 8, 10]
    sum_numbers : int = sum_number(numbers)
    print(f"The sum of {numbers} is {sum_numbers}.")

if __name__ == "__main__":
    main()

 
