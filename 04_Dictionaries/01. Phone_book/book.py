# Program 2: Creating a Phonebook
#In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    phone_book = {}
    while True:
        name = input("Enter Name: ")
        if name == "":
            break
        number = input("Enter Phone Number: ")
        phone_book[name] = number
    return phone_book

def print_phone_book(phone_book):
    for name in phone_book:
        print(name,":", phone_book[name])

def lookup_numbers(phone_book):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phone_book:
            print("Name not found.")
        else:
            print(phone_book[name])

def main():
    phone_book = read_phone_numbers()
    print_phone_book(phone_book)
    lookup_numbers(phone_book)

if __name__ == "__main__":
    main()

