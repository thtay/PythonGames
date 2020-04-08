# Hangman game
#

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

    answer = []
    for a in range(len(lettersGuessed)):
        for b in range(len(list(secretWord))):
            if list(secretWord)[b] == lettersGuessed[a]:
                answer.append(1)
                break
            else:
                answer.append(0)
    if sum(answer) == len(secretWord):
        log = True
    else:
        log = False
    return log


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    answerString = []
    for x in range(len(secretWord)):
        answerString.append(' _ ')
    for a in range(len(lettersGuessed)):
        for b in range(len(list(secretWord))):
            if list(secretWord)[b] == lettersGuessed[a]:
                answerString[b] = lettersGuessed[a]
    string = ''.join(answerString)
    return string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    import string
    fullAl = list(string.ascii_lowercase)
    for a in range(len(lettersGuessed)):
        fullAl.remove(lettersGuessed[a])
    stringFull = ''.join(fullAl)
    return stringFull


def repeatCheck(letter, lettersGuessed):
    for a in range(len(lettersGuessed)):
        counter = 0
        if letter == lettersGuessed[a]:
            return True

        else:
            counter += 1
            if counter == len(lettersGuessed):
                return False


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

    Follows the other limitations detailed in the problem write-up.
    '''

    lettersGuessed = []
    numGuess = 8
    myWord = getGuessedWord(secretWord, lettersGuessed)

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    while True:
        if numGuess == 0:
            break
        elif myWord == secretWord:
            break
        print('---------')
        print('You have ' + str(numGuess) + ' left.')
        availLetters = getAvailableLetters(lettersGuessed)
        print('Available Letters: ' + availLetters)
        guess = input('Please guess a Letter: ').lower()

        if repeatCheck(guess, lettersGuessed):
            print('Oops! You have already guessed that letter: ' + myWord)
        else:
            lettersGuessed.append(guess)
            if repeatCheck(guess, list(secretWord)):
                myWord = getGuessedWord(secretWord, lettersGuessed)
                print('Good guess: ' + myWord)
            else:
                numGuess = numGuess - 1
                myWord = getGuessedWord(secretWord, lettersGuessed)
                print('Oops! That letter is not in my word: ' + myWord)

    if numGuess == 0:
        print('---------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord)
    else:
        print('---------')
        print('Congratulations, you won!')


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
