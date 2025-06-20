#Project 5: Hangman python project

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' 'in word:
        word = random.choice(words)
    return word.upper()
    

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   #what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have ",lives, "lives left and you have used these letters",' '.join(used_letters))   # ' '.join(['a','b', 'cd']) --> a b cd

#To guess what the current word is:
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))


#Getting user input:
        user = input("Guess a letter: ").upper()
        if user in alphabet - used_letters:
            used_letters.add(user)
            if user in word_letters:
                word_letters.remove(user)
            else:
                lives = lives - 1
                print("letter is not in word")
            
        elif user in used_letters:
            print("You have already used that character. Please try again.")
            
        else:
            print("Invalid character. Please try again")

    #gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You died, sorry. The word was ", word)
    else:
        print("🎉🎉🎉Congrats!You guessed the word ", word, "!!")
    


hangman()
