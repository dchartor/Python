import random
WORDLIST_FILENAME = "words.txt"

def loadWords():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    tmp = ''
    for i in secretWord:
        if i in lettersGuessed:
            tmp += ' '.join(i)
        else:
            tmp += ' '.join('_')
    return tmp

def getAvailableLetters(lettersGuessed):
    import string
    allWord = string.ascii_lowercase
    for i in lettersGuessed:
        if i in allWord:
            allWord = allWord.replace(i, '')
    return allWord


def hangman(secretWord):
    import string
    print('Welcome to the game, Hangman!\nI am thinking of a word that is {0} letters long.'.format(len(secretWord)))
    print('------------')
    guessLet = []
    amTry = 8

    while amTry != 0:
        print('You have {0} guesses left.'.format(amTry))
        print('Available letters: {0}'.format(getAvailableLetters(guessLet)))
        guess = input('Please guess a letter: ').lower()

        if guess not in secretWord:
            guessLet.append(guess)
            print('Oops! That letter is not in my word: {0}'.format(getGuessedWord(secretWord, guessLet)))
            print('------------')
            if amTry == 1 and not isWordGuessed(secretWord, guessLet):
                print('Sorry, you ran out of guesses. The word was else.')
                print('The word was {0}'.format(secretWord))
            amTry -= 1
        elif guess in guessLet:
            print("Oops! You've already guessed that letter: {0}".format(getGuessedWord(secretWord, guessLet)))
            print('------------')
        elif guess in secretWord:
            guessLet.append(guess)
            print('Good guess: {0}'.format(getGuessedWord(secretWord, guessLet)))
            print('------------')
        if isWordGuessed(secretWord, guessLet):
            print('Congratulations, you won!')
            break

            
if __name__ == '__main__':
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
