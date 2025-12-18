import random
import string
import json

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

def hangMan():
    # define the alphabet
    alphabet = set(string.ascii_uppercase)
    # get valid word
    word = get_valid_word(myList)
    # store as string for literal comparison, removing the tailing newline character
    wordString = word.upper()[:-1]
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
    for let in word:
        length += '-'
    print(length)
    while wordString != showTing:
        #if len(letters) > 0:
            #print("Successfull guesses: ", " ".join(letters))
        # list guessed letters that do not exist in the word
        if len(failLetters) > 0:
            print("Unsuccessful guesses: ", " ".join(failLetters) + "\n")
        # user prompt that gets guess in uper case
        user_letter = input("Guess a letter: ").upper()
        #print(word)
        # makes sure that guess is a single character and that it exists in the alphabet
        if len(user_letter) == 1 and user_letter in alphabet:
            # adds guess to list of valid letters if it exists in the word but if it already exists as a valid guess
            if user_letter in word and user_letter not in letters:
                letters.append(user_letter)
                #wordLets.remove(user_letter)
            # adds guess to list of letters not in word unless it already exists as a failed guess
            elif user_letter not in failLetters and user_letter not in letters:
                failLetters.append(user_letter)
                print("Sorry, try again\n")
        # alerts user that their input is invalid
        else:
            print("Invalid input; guess a single letter\n")
        # initializes an empty string for display to user and as the ultimate comparative value
        showTing = ''
        # builds string
        for user_letter in word:
            if user_letter in letters:
                showTing += user_letter
            else:
                showTing += "-"
        print(showTing + "\n")

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