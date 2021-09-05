# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:09:50 2021

@author: ENkanga
"""

low = 0
high = 100
cut = ''

print('Please think of a number between 0 and 100!')
while cut != 'c':
    guess = int((high + low) / 2)
    print('Is your secret number ' + str(guess) + '?')
    cut = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if cut not in ['h', 'l', 'c']:
        print('Sorry, I did not understand your input.')
        continue
    elif cut == 'l':
        low = guess
    elif cut == 'h':
        high = guess
print('Game over. Your secret number was:', guess)
    