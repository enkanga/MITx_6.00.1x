# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 13:19:38 2021

@author: ENkanga
"""

'''
Consider the following sequence of expressions:
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

Write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.
'''

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    total = 0
    for val in aDict.values():
        total += len(val)
    return total
    