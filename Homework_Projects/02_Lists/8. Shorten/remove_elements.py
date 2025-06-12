# Program 8: Removing the last elements from the list 
# and then printing those elements until the length (Max-legth) of the list becomes 3.

#Question:
#Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. 
# We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        print(lst.pop())

def get_lst():
    """
    This will get the integer from the user one at a time and returns the resulting list.

    """
    lst = []
    element = input("Enter an integer (or press 'enter' to finish): ")
    while element != "":
        lst.append(element)
        element = input("Enter an integer (or press 'enter' to finish): ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("The final list is: ", lst)

if __name__ == "__main__":
    main()
        
