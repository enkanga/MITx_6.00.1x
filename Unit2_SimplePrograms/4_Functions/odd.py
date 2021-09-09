# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:39:42 2021

@author: ENkanga
"""

'''
Write a Python function, odd, that takes in one number 
and returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.
'''

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return bool(x % 2)