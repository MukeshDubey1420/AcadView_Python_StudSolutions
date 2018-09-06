import random

# Global Variables
d = {'barnyard':'place', 'airplane':'transportation', 'daughter':'loved     ones',
 'vacuum':'object', 'elevator':'transportation', 'football':'sport', 'swimming':'sport',
 'lemonade':'food and drink', 'handsome':'appearance', 'racoon':'animal'}
randomWord = ''
randomWordGenre = ''
matchedChar = []
displaySpaces = []
characterList = []

def main():
    while True:
        playAgain = ('y')
        while playAgain == 'y':
            gameLayout()
            resetGame()

            # Get random word, genre and split word into list.
            getRandomWord()
            getRandomWordGenre()
            getCharacterList()

            # Prompt user for level.
            gameMode = input('Choose a level.')
            if gameMode == 'easy':
                numberOfGuesses = 10
            elif gameMode == 'medium':
                numberOfGuesses = 8
            elif gameMode == 'hard':
                numberOfGuesses = 7

            # Display blank spaces and genre of word.
            print('Genre: ' + randomWordGenre)
            displayBlankSpaces()
            joinDisplaySpaces()

            # Run main game loop.
            guesses = 0
            while guesses < numberOfGuesses and checkChar() == False:
                guess = input('Enter a character. You have ' + str(numberOfGuesses - guesses) + ' guesses left.')
                matchGuess(guess)
                addGuessedCharacters()
                joinDisplaySpaces()
                if checkChar() == True:
                    print('Congratulations. You just won Hangman!')
                elif matchGuess(guess) == False:
                    guesses += 1
            if guesses == numberOfGuesses:
                print('Sorry, you lost.')
            playAgain = input('Would you like to play again? (y/n)')
        break

# Game Layout
def gameLayout():
    print ('++++++++++++++++++Hangman++++++++++++++++++++++')
    print ('===============================================')
    print ('|--  Level  --|--  Tries  --|-- Hints Given --|')
    print ('|--  Easy   --|--   10    --|--      2      --|')
    print ('|--  Medium --|--    8    --|--      1      --|')
    print ('|--  Hard   --|--    7    --|--      0      --|')

# Reset game processes.
def resetGame():
    global randomWord, randomWordGenre, matchedChar, displaySpaces, numberOfCharacters, characterList
    randomWord = ''
    randomWordGenre = ''
    matchedChar = []
    displaySpaces = []
    numberOfCharacters = 0
    characterList = []

# Get a random word from dictionary and store in global
# variable getRandomWord[]
def getRandomWord():
    global randomWord
    randomWord = random.choice(list(d.keys()))

# Get genre from chose random word and store in global
# variable randomWordGenre[]
def getRandomWordGenre():
    global randomWordGenre
    randomWordGenre = d[randomWord]

# Split string into character list and store in global
# variable characterList[]
def getCharacterList():
    for char in range(0, len(randomWord)):
        characterList.append(randomWord[char])

# Check if user guess matches any character(s) of word and saves
# index position(s) to global variable matchedChar[]
def matchGuess(guess):
    if guess in characterList:
        index = 0
        while index < len(randomWord):
            index = randomWord.find(guess, index)
            if index == -1:
                break
            matchedChar.append(index)
            index += 1
    else:
        return False

# Display blank spaces for # of characters in word and stores in
# global variable displaySpaces[]
def displayBlankSpaces():
    for x in range (0, len(characterList)):
        displaySpaces.append("_")
    return displaySpaces

# Add guessed characters to global variable displaySpaces[]
def addGuessedCharacters():
    for x in range (0, len(matchedChar)):
        displaySpaces[matchedChar[x]] = randomWord[matchedChar[x]]

# Check if all guessed characters match word and return True or False.
def checkChar():
    str1 = ''.join(str(e) for e in displaySpaces)
    return str1 == randomWord

def joinDisplaySpaces():
    str1 = ' '.join(str(e) for e in displaySpaces)
    print (str1)

main()
