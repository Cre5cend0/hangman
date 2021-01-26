# Hangman game

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    li = sorted(secretWord)
    l = []
    for i in li:
        if i in lettersGuessed:
            l.append(i)
    if sorted(l) == li:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = len(secretWord) * '_'
    secret = list(word)
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            secret.insert(count, i)
            secret.pop(count + 1)
            count += 1
        else:
            count += 1
            continue

    def listtostr(li):
        new = " "
        return new.join(li)

    return listtostr(secret)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

    for char in lettersGuessed:
        if char not in letters:
            continue
        letters.pop(letters.index(char))

    def listtostr(li):  # this function is defined earlier too
        new = " "
        return new.join(li)

    return listtostr(letters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    username = input("Please input your name: ")
    print("\nHi " + username + ". Welcome to the game, Hangman!")

    if len(secretWord) == 8 or len(secretWord) == 11:
        print('I am thinking of an ' + str(len(secretWord)) + ' letter word.')
    else:
        print('I am thinking of a ' + str(len(secretWord)) + ' letter word.')

    print('-' * 48)

    lettersGuessed = []
    guesses = 8
    print('Number of guesses left: ' + str(guesses))

    while not isWordGuessed(secretWord, lettersGuessed):

        print('Available letters: ' + getAvailableLetters(lettersGuessed))

        guess = input('Please guess a letter: ')

        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess not in secretWord:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed) + "\n")
                guesses -= 1
                print('Number of guesses left: ' + str(guesses))
            else:
                print('Good Guess ' + getGuessedWord(secretWord, lettersGuessed) + "\n")

        else:
            print('You have already guessed this letter.', guess + "\n")

        if guesses == 0:
            print('You have run out of Guesses. Try again next time.')
            print('The word was ' + secretWord)
            print("#" * 45)
            break
    else:
        print('Congratulations! ' + username + '.' + ' You have guessed the word: ' + secretWord)


if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
