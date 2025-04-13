# Program 6: Getting the last element of a list.
#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. 
#The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    """
    This will print the last element of the list
    
    """
    print(lst[len(lst)-1])

def get_lst():
    """
    This will get one element from the user and returns the resulting list

    """
    lst = []
    element = input("Enter an element (or press 'enter' to finish): ")
    while element != "":
        lst.append(element)
        element = input("Enter an element (or press 'enter' to finish): ")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":
    main()