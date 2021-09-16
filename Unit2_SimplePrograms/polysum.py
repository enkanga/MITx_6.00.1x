# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:08:30 2021

@author: ENkanga
"""

'''
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: (0.25 * n * s^2) / (tan(pi / n))
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.
'''

from math import tan, pi

def polysum(n, s):
    '''
    Parameters
    ----------
    n : int
        number of sides of polygon.
    s : float
        length of each side of polygon.

    Returns
    -------
    ans : float
          sum of area and squared perimeter of polygon.

    '''
    area = (0.25 * n * s**2) / tan(pi / n)
    perimeter = n * s
    
    return round(area + perimeter**2, 4)