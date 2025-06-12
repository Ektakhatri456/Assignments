# Program 2: Doubling Elements in a List
# This program takes a list of numbers and doubles each element in the list.

# Write a program that doubles each element in a list of numbers.

def double_elements(numbers):
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    return doubled

def main():
    original = [1, 3, 5, 7, 9]
    print("Original List:", original)
    
    result = double_elements(original)
    print("Modified List:", result)

if __name__ == "__main__":
    main()