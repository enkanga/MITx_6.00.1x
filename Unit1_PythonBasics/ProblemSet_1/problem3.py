# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:31:55 2021

@author: ENkanga
"""

'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s 
in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print:
Longest substring in alphabetical order is: abc
'''

s = 'azcbobobegghakl'
sub_str = ''
for i in range(len(s)):
    curr_str = ''
    for j in range(i, len(s)): 
        curr_str += s[j]
        if j == len(s) - 1:
            break
        elif s[j] > s[j + 1]:
            break
    if len(curr_str) > len(sub_str):
        sub_str = curr_str
print('Longest substring in alphabetical order is:', sub_str)