# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:09:50 2021

@author: ENkanga
"""

'''
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, 
and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!

Your initial endpoints should be 0 and 100. 
Do not optimize your subsequent endpoints by making them be 
the halfway point plus or minus 1. Rather, just make them be the halfway point.
When the user enters something invalid, you should print out a message 
to the user explaining you did not understand their input.
'''
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
    