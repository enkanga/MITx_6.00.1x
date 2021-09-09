# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:30:58 2021

@author: ENkanga
"""

'''
Write a Python function, fourthPower, that takes in one number and returns 
that value raised to the fourth power.

You should use the square procedure that you defined in an earlier exercise.

This function takes in one number and returns one number.
'''
from square import square

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(square(x))
