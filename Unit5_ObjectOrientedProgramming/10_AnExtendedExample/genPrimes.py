# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:11:03 2021

@author: ENkanga
"""

'''
Write a generator, genPrimes, that returns the sequence of prime numbers on 
successive calls to its next() method: 
    2, 3, 5, 7, 11, ...
'''

def genPrimes():
    primes = [2]
    
    while True:
        yield primes[-1]
        
        test_prime = primes[-1] + 1
        
        cont = True
        
        while cont:
            for prime in primes:
                if test_prime % prime == 0:
                    test_prime += 1
                    break
           
            else:   # executed if iterable `for prime in primes` is exhausted
                cont = False
            
        primes.append(test_prime)
    
            
primes = genPrimes()

for i in range(5):
    print(next(primes))