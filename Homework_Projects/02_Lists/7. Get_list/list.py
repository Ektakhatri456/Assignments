# Program 7: Adding elements into the list one by one.
#Write a program which continuously asks the user to enter values which are added one by one into a list. 
#When the user presses enter without typing anything, print the list.

def main():
    lst = []
    element = input("Enter an element: ")
    while element:
        lst.append(element)
        element = input("Enter an element: ")
    print("Final list:", lst)

if __name__ == "__main__":
    main()