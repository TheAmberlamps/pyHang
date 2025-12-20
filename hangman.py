from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

print("loading")

chrome_options = Options()

chrome_options.add_argument("--headless=new")

driver= webdriver.Chrome(options=chrome_options)

url = 'https://www.randomlists.com/random-words?qty=1&dup=false'

driver.get(url)

#print(f"url title: {driver.title}")

found_word = driver.find_element(By.CLASS_NAME, "base_title__Yd1Gv").text.upper()

#print(f"found word: {found_word}")

driver.quit()

#import random
import string
import platform
import os

def clrScr():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Deprecated
#file_path = 'word_list.txt'

#myList = []

#with open(file_path, 'r') as file:
    #myList = file.readlines()

#def get_valid_word(myList):
    #word = random.choice(myList)
    # below is important; multiple conditionals have to be evaluated to their specific values even if it's alwayys the same.
    # never forget that programming is explaining to a complex rock in excruciating detail how to do the things we think of as simple.
    #while '-' in word or ' ' in word:
        #word = random.choice(word)
    #print('\n' + word)
    #return word

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
    word = found_word
    # store as string for literal comparison, breaking it apart via whitespaces 
    wordString = ' '.join(word)
    # the below seems repetitive and dumb since I already have the word and am splitting it apart... maybe take a minute to examine this
    # spread word into a list
    word = list(word)
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
        # so to explain, this is creating a conditional list based on whether any given letter in the word has been guessed or not, then splits that list apart with whitespaces.
        showTing = ' '.join([letter if letter in letters else '_' for letter in word])
        #print(wordString)
        updater(lives)
        print(f'Guesses left: {lives}\n')
        print(showTing + '\n')
    print("Congratulations! You win!")

hangMan()