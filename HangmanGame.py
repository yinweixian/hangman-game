#matthew walker
#Hangman Game
#nov 26

import random

HANGMAN = (
"""
--------
|      |
|
|
|
|
|
|
|
|
|
|
------------
"""
,
"""
--------
|      |
|      0
|
|
|
|
|
|
|
|
|
------------
"""
,
"""
--------
|      |
|      0
|     / \\
|    /   \\
|   /     \\
|      
|      
|
|
|
|
------------
"""
,
"""
--------
|      |
|      0
|     /|\\
|    / | \\
|   /  |  \\
|      |
|      |
|
|
|
|
------------
"""
,
"""
--------
|      |
|      0
|     /|\\
|    / | \\
|   /  |  \\
|      |
|      |
|     |
|     |
|     |
|
------------
"""
,
"""
--------
|      |
|      0
|     /|\\
|    / | \\
|   /  |  \\
|      |
|      |
|     | |
|     | |
|     | |
|
------------
""")
MAXWRONG = len(HANGMAN)-1
WORDS = ("INPUT","HEY","HI","HAI","WASSUP","MEATBALL","POTATO","BEKFAST","LUCARIO","LINK")
#initialize variables
word = random.choice(WORDS)#the word to be guessed
soFar = "-"*len(word)#one dash for each letter in word to be guessed
wrong = 0#number of wrong guesses player has made
used = []#letters already guessed

print("Welcome to Hangman. Good luck!")#intro to the game
#main loop
while wrong < MAXWRONG and soFar != word:#while conditions
    print(HANGMAN[wrong])
    print("\nYouve used the following letters:\n",used)
    print("\nSo far, the word is:\n", soFar)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
    while guess in used:
        print("You've already guessed the letter",guess)
        guess = input("Enter your guess:")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nYes!",guess,"is in the word!")
        new = ""


        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += soFar[i]
        soFar = new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong += 1

if wrong == MAXWRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was",word)

input("\n\nPress the enter key to exit.")
        













































































    



