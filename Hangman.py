# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:27:37 2020

Hangman using words.txt as word source

"""

import random
import sys

# Load word list
with open('words.txt', 'r') as f:
    wordlist = f.read().split('\n')
# Prep alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def displayboard(secret, solved, lives, used):
    
    print('\n--- Hangman ---\n\n')
    
    # Print secret word with _ as necessary
    print('Secret Word:')
    wordstr = ''
    for i in range(len(solved)):
        if solved[i]:
            wordstr += secret[i] + ' '
        else:
            wordstr += '_ '
    print(wordstr + '\n\n')
    
    # Print lives and past guesses
    wordstr = 'Lives left: '
    for i in range(lives):
        wordstr += '♥ '
    print(wordstr)
    print('Past guesses:', used)


def main():
    
    # Empty list of used letters    
    used = []
    
    # Set number of lives
    lives = 6
    
    # Set secret word
    secret = random.choice(wordlist).upper()
    solved = []
    for i in range(len(secret)):
        solved.append(False)
    
    # Set gamestate 0=next turn, 1=lost game, 2=won game
    gamestate = 0
    
    while True:
        
        displayboard(secret, solved, lives, used)
        
        # Player turn
        if gamestate == 0:
            
            # Get valid letter choice
            valid = False
            while not valid:
                choice = input('Your guess (A-Z, 0 to quit)? ').upper()
                if choice == '0':
                    sys.exit()
                elif len(choice) != 1 or not choice.isalpha():
                    print('Please try one letter at a time!')
                elif choice in used:
                    print('This letter has been tried before!')
                else:
                    used.append(choice)
                    valid = True
                    print('\n')
            
            # Check if choice in secret
            success = False
            for i in range(len(secret)):
                if choice == secret[i]:
                    success = True
                    solved[i] = True
            if not success:
                lives += -1
                if lives == 0:
                    gamestate = 1
            else:
                win = True
                for i in solved:
                    win = win and i
                if win:
                    gamestate = 2
        
        # Out of lives
        elif gamestate == 1:
            
            print('Sorry, you have run out of lives!')
            print('The secret word is ' + secret)
            return
        
        # Win game
        else:
            
            print('You win! Well done!')
            return

while True:
    
    main()
    if input('\nPlay again (y/n)? ').lower() == 'n':
        sys.exit()
    
