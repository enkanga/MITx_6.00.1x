# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:30:33 2021

@author: ENkanga
"""

'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
Number of times bob occurs is: 2
'''

# s = 'abcdefghijklmnopqrstuvwxyz'
num_bob = 0
for i in range(len(s)):
    if s[i : i + 3] == 'bob':
        num_bob += 1
print('Number of times bob occurs is:', num_bob)