
# Hangman is a word puzzle game that is typically played by two or more people. The goal of the game is for one player (the "guesser") to guess a hidden word or phrase, one letter at a time, before they run out of chances. The other player (the "word provider") selects the word or phrase and keeps it hidden.

# Here are the basic rules of the Hangman game:

# Word or Phrase Selection:

# The word provider selects a word or phrase, which is typically a common English word, a short phrase, or a proper noun. The word or phrase is kept secret from the guesser.
# Drawing the Hangman:

# A hangman figure is drawn with several empty spaces or lines, representing the number of letters in the word or phrase. The number of lines usually corresponds to the number of letters in the word.
# Guessing Letters:

# The guesser starts by guessing one letter at a time. They can guess any letter of the alphabet.
# If the guessed letter is in the word or phrase, the word provider reveals all instances of that letter in the correct positions on the hangman figure.
# If the guessed letter is not in the word or phrase, the word provider starts to draw parts of a hangman (typically starting with the head, then the body, arms, and legs) as incorrect guesses accumulate.
# Word Completion:

# The guesser continues guessing letters until they either guess the entire word correctly or make a certain number of incorrect guesses, resulting in the completion of the hangman figure.
# Winning or Losing:

# The game is won by the guesser if they correctly guess the word or phrase before the hangman is completely drawn.
# The game is lost by the guesser if the hangman figure is completed before they guess the word.
# Clues:

# Some variations of Hangman allow for the word provider to give the guesser a limited number of clues, which might be a definition, a category, or a hint related to the word or phrase.
# Game Over:

# Once the game is over (whether the guesser wins or loses), the word provider reveals the hidden word or phrase.







import random
from words import words
import string

# our list of words have some error some words have comma and underscore so we donot have to take that words
def get_valid_words(words):
    word=random.choice(words) #randomly choose something from list  
    while " " in word or "-"  or ','in word:
         word=random.choice(words)
    return word



def hangman():
     #for initialization
     word_letters=['A']
     
     while len(word_letters)>0:
          #letters used
          print("You have used these letters: " .join(used_letters))

          #what current words is (i.e W _ R D)
          word_list=[letter if letter in used_letters else ' 'for letter in word]
          print("Current Word: "," ".join(word_list))

          word=get_valid_words(words)
          word_letters=set(word)  # stores letters of word ,search set function on google if dont know
          alphabet=set(string.ascii_uppercase)#this will give a set of A To Z
          used_letters=set()#keep track what user has guessed
          #letters used
          print("You have used these letters: " .join(used_letters))

          #getting user input
          user_letter=input("Guess A Letter: ").upper()

          if user_letter in alphabet-used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                     word_letters.remove(user_letter)
          elif user_letter in used_letters:
                print("You Have Already Used that Character.Please Try Again.")
          else:
                print("Invalid Character.Please Try Again")

hangman()




