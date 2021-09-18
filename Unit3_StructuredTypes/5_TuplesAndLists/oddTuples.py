# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:43:05 2021

@author: ENkanga
"""

'''
Write a procedure called oddTuples, which takes a tuple as input, 
and returns a new tuple as output, where every other element of the input tuple is copied, 
starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    output = ()
    for i in range(len(aTup)):
        if not i % 2:
            output += (aTup[i],)
    return output

"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[::2]
"""

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
        