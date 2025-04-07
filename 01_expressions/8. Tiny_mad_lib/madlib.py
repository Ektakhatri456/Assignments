# Program 8: Creating tiny madlib
#Write a program which prompts the user for an adjective, then a noun,
#  then a verb, and then prints a fun sentence with those words!

def main():

    sentence_start : str = "Python is Awesome! With just a few words, I made my"

    noun : str = input("Please type a noun and press enter: ")
    verb : str = input("Please type a verb and press enter: ")
    adjective : str = input("Please type an adjective and press enter: ")

    print(f"{sentence_start} {noun} {verb} {adjective} across the screen!")

if __name__ == "__main__":
    main()
