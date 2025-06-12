# Program 5: Getting first element from the list
#Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list.
#The list is guaranteed to be non-empty.

def get_first_element(lst):
    """
    This function takes a list as input and returns the first element of the list.
    
    """
    print(lst[0])

def get_lst():
    """
    This will prompt the user to enter one element of the list at a time and returns the resulting list. 
    
    """
    lst = []
    element : str = input("Enter the elememt of the list: ")
    while element != "":
        lst.append(element)
        element = input("Enter the element of the list: ")
        return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == "__main__":
    main()