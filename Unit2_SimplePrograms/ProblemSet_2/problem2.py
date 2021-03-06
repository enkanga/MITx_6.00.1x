# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:49:45 2021

@author: ENkanga
"""

'''
Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment 
that will pay off all debt in under 1 year, for example:
Lowest Payment: 180 

Assume that the interest is compounded monthly according to 
the balance at the end of the month (after the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance to become negative using this payment scheme, 
which is okay. 

A summary of the required math is found below:
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

def minFixedMonthlyPayment(balance, annualInterestRate):
    '''
    Calculates the minimum fixed monthly payment needed 
    in order pay off a credit card balance within 12 months.

    Parameters
    ----------
    balance : float
        the outstanding balance on the credit card.
    annualInterestRate : float
        annual interest rate.

    Returns
    -------
    minMothlyPayment : int
        the lowest monthly payment that will pay off all debt in under 1 year.

    '''
    monthlyInterestRate = annualInterestRate / 12.0
    og_balance = balance
    
    monthlyPayment = 10
    while balance > 0:
        balance = og_balance
        for i in range(12):
            monthlyUnpaidBalance = balance - monthlyPayment
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
        if balance <= 0:
            return monthlyPayment
        else:
            monthlyPayment += 10
            
print('Lowest Payment:', minFixedMonthlyPayment(3329, 0.2))