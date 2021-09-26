# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:57:08 2021

@author: ENkanga
"""

'''
When we call 

    print(integerDivision(5, 3))
    
we get the following error message:
    
    File "temp.py", line 9, in integerDivision
        count += 1
    UnboundLocalError: local variable 'count' referenced before assignment

Modify the code for integerDivision so that this error does not occur.
'''

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(5, 3))