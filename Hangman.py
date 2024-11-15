import random
import string
from words import words

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) #letters in the guessed word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        #letters used 
        #' '.join(['a','b','ed']) --> 'a b ed'

        print(f"You have {lives} lives left")

        print("You have guessed these letters: ",' '.join(used_letters))
        
        new_word = ""
        for letter in word:
            if letter in used_letters:
                new_word += letter
            else:
                new_word += "_"
            new_word += " "

        print("Current word: ",' '.join(new_word))
        if "_" not in new_word:
            print("Woohoo!You have cracked the word")
            break

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Right Guess")
            else:
                lives = lives-1
                print("Wrong Guess")
        elif user_letter in used_letters:
            print("You have already used that. Please try again!")
        
        else:
            print("You didn't type a valid character. Please try again!")

        if "_" in new_word and lives == 0:
            print(f"The word is {word}")
    

hangman()

    