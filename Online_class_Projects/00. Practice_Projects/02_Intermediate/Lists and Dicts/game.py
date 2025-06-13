# Problem: List playzone...

def access_element(my_list, index):
    if index >= 0 and index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."
    
def modify_element(my_list, index, new_value):
    if index >= 0 and index < len(my_list):
        my_list[index] = new_value
        return my_list
    else:
        return "Index out of range."
    
def slice_list(my_list, start, end):
    if 0 <= start and end <= len(my_list) and start < end:
        return my_list[start : end]
    else:
        return "Invalid slice range."
    
def main_game():
    my_list = [10, 20, 30, 40, 50]

    print("Choose an operation: access / modify / slice")
    choice = input("Enter your choice: ").lower()

    if choice == "access":
        index = int(input("Enter index to access: "))
        print("Element at index", index, "is: ", access_element(my_list, index))

    elif choice == "modify":
        index = int(input("Enter index to modify: "))
        new_value = int(input("Enter new value: "))
        print("Modified list: ", modify_element(my_list, index, new_value))

    elif choice == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced list: ", slice_list(my_list, start, end))

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_game()