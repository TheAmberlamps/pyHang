import random
import string
import json
import platform
import os

def clrScr():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

file_path = 'word_list.txt'

myList = []

with open(file_path, 'r') as file:
    myList = file.readlines()

def get_valid_word(myList):
    word = random.choice(myList)
    # below is important; multiple conditionals have to be evaluated to their specific values even if it's alwayys the same.
    # never forget that programming is explaining to a complex rock in excruciating detail how to do the things we think of as simple.
    while '-' in word or ' ' in word:
        word = random.choice(word)
    #print('\n' + word)
    return word

def drawGuy(lives):
    def default():
        print("|")    
    print("_____")
    print("|   |")
    if lives < 6:
        print("|   o")
    else:
        default()
    if lives < 5:
        if lives == 4:
            print("|   |")
        elif lives == 3:
            print("|  -|")
        else:
            print("|  -|-")
    else:
        default()
    if lives < 2:
        if lives == 1:
            print("|   /")
        else:
            print("|   /\\")
    else:
        default()
    print("|\n")

def hangMan():
    # define the alphabet
    alphabet = set(string.ascii_uppercase)
    # get valid word
    word = get_valid_word(myList)
    # store as string for literal comparison, breaking it apart via whitespaces and removing the tailing newline character
    #wordString = word.upper()[:-1]
    wordString = ' '.join((word.upper()[:-1]))
    # the below seems repetitive and dumb since I already have the word and am splitting it apart... maybe take a minute to examine this
    # spread word into a list
    word = list(word)
    # remove newline character from end of list
    word.pop()
    # convert all entries in list to upper case
    word = [ting.upper() for ting in word]
    # stores letters that exist in list
    letters = []
    # stores letters that do not exist in list
    failLetters = []
    # current guess string
    showTing = ''
    #print(f"wordLets: {word}")
    length = ""

    def updater(lives):
        clrScr()
        drawGuy(lives)

    lives = 6
    updater(lives)
    for let in word:
        length += '_ '
    print(length + '\n')
    while wordString != showTing and lives > 0:
        # list guessed letters that do not exist in the word
        if len(failLetters) > 0:
            print("Unsuccessful guesses: ", " ".join(failLetters) + "\n")
        # user prompt that gets guess in upper case
        user_letter = input("Guess a letter: ").upper()
        print("\n")
        #print(word)
        # makes sure that guess is a single character and that it exists in the alphabet
        if user_letter in alphabet:
            # adds guess to list of valid letters if it exists in the word but if it already exists as a valid guess
            if user_letter in word and user_letter not in letters:
                letters.append(user_letter)
                #wordLets.remove(user_letter)
            # adds guess to list of letters not in word unless it already exists as a failed guess
            elif user_letter not in failLetters and user_letter not in letters:
                lives = lives -1
                if lives < 1 :
                    updater(lives)
                    print(f"Game over! The word was {wordString}")
                    return
                else:
                    failLetters.append(user_letter)
                    print("Sorry, try again\n")
        # alerts user that their input is invalid
        #else:
            #print("Invalid input, try again.\n")
        # this is the commented-out implementation that I created, which works fine. Beneath it is the version used by the person that wrote the tutorial I followed. They both have value.

        # initializes an empty string for display to user and as the ultimate comparative value
        # builds string
        #showTing = ''
        #for user_letter in word:
            #if user_letter in letters:
                #showTing += user_letter
            #else:
                #showTing += "-"

        # so to explain, this is creating a conditional list based on whether any given letter in the word has been guessed or not, then splits that list apart with whitespaces.
        showTing = ' '.join([letter if letter in letters else '_' for letter in word])

        #print(wordString)
        updater(lives)
        print(f'Guesses left: {lives}\n')
        print(showTing + '\n')
    print("Congratulations! You win!")

hangMan()
# crazy, Python includes hidden characters to its strings... they really aren't kidding when they talk about how much more strict this language is in comparison to javascript
#word = 'antifascism'
#word = myList[22534]
#wordActual = repr(word)
#wordActual = f'{word}\n'

# OK, so I need to explicitly save each entry as a string... maybe use the str() method to coerce type?

# At any rate this has let me learn a load! Making some actual progress learning Python has been fun, even if it's all CLI and scraping so far

#with open('words_dictionary.json', 'r') as file:
    #data = json.load(file)
    #random_pair = random.choice(list(data.items()))
    #print(random_pair[0])
    #print(len(myList))
    #for keys in data.keys():
        #myList.append(f'{keys}\n')

#print(len(myList))
#print(type(myList))

#with open(file_path, 'w', encoding="utf-8") as file:
    #file.writelines(myList)