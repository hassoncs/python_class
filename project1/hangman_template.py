# Name: Joel Shooster
# MIT Username:
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = ''
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    letters_guessed = "".join(letters_guessed)
    for i in secret_word:
        if i not in letters_guessed.lower():
            return False
    print "You won! Congratulations!"
    print secret_word
    return True



def print_guessed():
    '''
    Returns a string that contains the word with a dash "-" in
    place of letters not guessed yet.
    '''
    global secret_word
    global letters_guessed

    output = []
    letters_guessed = "".join(letters_guessed)
    letters_guessed = letters_guessed.lower()
    for i in secret_word:
        if i not in letters_guessed:
            output.append("-")
        else:
            output.append(i)
    print "".join(output)

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()
    game_over = False
    print "Art created by sk"
    letters = "abcdefghijklmnopqrstuvwxyz"
    answer_correct = None

    while game_over == False:
        print "\n%s guesses left" % (MAX_GUESSES - mistakes_made)
        print_hangman_image(mistakes_made)
        print_guessed()
        guess = raw_input("\nEnter a letter: ")
        for i in letters:
            while guess not in letters:
                guess = raw_input("Not a valid option. Guess again:\n")
            else:
                letters_guessed += guess
        letters = letters.replace(guess, "")
        print "Available letters: [", letters, "]"
        for i in secret_word:
            if guess in secret_word:
                answer_correct = True
            else:
                answer_correct = False
        if answer_correct == True:
            print "Good guess!"
        else:
            print "Wrong!"
            mistakes_made = mistakes_made + 1
        if mistakes_made == 6:
            print_hangman_image(mistakes_made)
            print "Game Over! You lost!"
            print "The correct answer was: %s" % secret_word
            game_over = True
        if word_guessed() == True:
            game_over = True

play_hangman()
