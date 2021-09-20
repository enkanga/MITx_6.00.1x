# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 13:39:16 2021

@author: ENkanga
"""

'''
Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

Write a procedure, called biggest, which returns the key corresponding to 
the entry with the largest number of values associated with it. 
If there is more than one such entry, return any one of the matching keys.

If there are no values in the dictionary, biggest should return None.
'''

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict) > 0:
        largest_num_vals = max(map(len, aDict.values()))
        for k in aDict.keys():
            if len(aDict[k]) == largest_num_vals:
                return k 
    else:
        return None

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
    