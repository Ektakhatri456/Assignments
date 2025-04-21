# Program 4: Prompting the user to write the exact affirmation message.
#Question:
#Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!
#Here's a sample run of the program (user input is in blue):
#Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)
#Note that you can call input() with no prompt and it will still wait for a user to type something!

Affirmation : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please enter the exact affirmation message: " + Affirmation)
    user_input = input()
    while user_input != Affirmation:
        print("Hmm, that was not the affirmation. Please try again.")
        user_input = input()
    print("That's right! 😊")

if __name__ == "__main__":
    main()