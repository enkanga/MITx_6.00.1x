# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 19:39:59 2021

@author: ENkanga
"""

'''
Here is the code for a function applyToEach:
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

Assume that testList = [1, -4, 8, -9]
For each of the following questions, provide an expression using applyToEach, 
so that after evaluation testList has the indicated value.
'''
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
#%% apply to each 1
"""
>>> print(testList)
[1, 4, 8, 9]
"""
testList = [1, -4, 8, -9]

def absoluteValue(a):
    '''
    Parameters
    ----------
    a : an integer.

    Returns
    -------
    the absolute value of a.
    
    '''
    if a >= 0:
        return a
    else:
        return -a

applyToEach(testList, absoluteValue)
print(testList)

#%% apply to each 2
"""
>>> print(testList)
[2, -3, 9, -8]
"""
testList = [1, -4, 8, -9]

def addOne(a):
    '''
    Parameters
    ----------
    a : an integer.

    Returns
    -------
    1 + a.
    
    '''
    return 1 + a

applyToEach(testList, addOne)
print(testList)

#%% apply to each 3
"""
>>> print(testList)
[1, 16, 64, 81]
"""
testList = [1, -4, 8, -9]

def squared(a):
    '''
    Parameters
    ----------
    a : an integer.

    Returns
    -------
    a^2.
    
    '''
    return a**2

applyToEach(testList, squared)
print(testList)