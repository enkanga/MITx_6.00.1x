# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:33:35 2021

@author: ENkanga
"""

'''
Write an iterative function iterPower(base, exp) 
that calculates the exponential by simply using successive multiplication. 
For example, iterPower(base, exp) should compute base^exp 
by multiplying base times itself exp times.

This function should take in two values - base can be a float or an integer; 
exp will be an integer >= 0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed.
'''

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    ans = 1
    for i in range(exp):
        ans *= base
    return ans
        