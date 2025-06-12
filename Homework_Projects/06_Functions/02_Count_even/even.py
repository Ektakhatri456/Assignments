# Program 3: Counting Even Numbers from User Input

# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.


def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def get_list_of_integers():
    lst = []
    while True:
        user_input = input("Enter an integer (or press enter to stop):  ")
        if user_input == "":
            break
        lst.append(int(user_input))
    return lst

def main():
    lst = get_list_of_integers()
    count_even(lst)

if __name__ ==  "__main__":
    main()