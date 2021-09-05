# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:53:54 2021

@author: ENkanga
"""

#%% x < 1

cube = -54
epsilon = 0.01
num_guesses = 0
low = cube
high = 0
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    print('low =', str(low), 'high =', str(high), 'guess =', str(guess))
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

#%% -1 < x < 0

# cube = -0.1
epsilon = 0.001
num_guesses = 0
low = -1
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    print('low =', str(low), 'high =', str(high), 'guess =', str(guess))
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

#%% 0 < x < 1

cube = 0.1
epsilon = 0.001
num_guesses = 0
low = cube
high = 1
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    print('low =', str(low), 'high =', str(high), 'guess =', str(guess))
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)


