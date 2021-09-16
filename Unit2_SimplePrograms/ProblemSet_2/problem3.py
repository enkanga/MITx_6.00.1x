# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:07:42 2021

@author: ENkanga
"""

'''
Write a program that uses these bounds for the montly payment:
lower bound = One-twelfth of the original balance
upper bound = one-twelfth of the balance, after having its interest compounded monthly for an entire year.
    
and bisection search to find the smallest monthly payment to the cent 
(no more multiples of $10) such that we can pay off the debt within a year.
'''

def minFixedMonthlyPaymentBisection(balance, annualInterestRate):
    '''
    Calculates the minimum fixed monthly payment needed 
    in order pay off a credit card balance within 12 months using bisection search.

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
    
    lowerBound = balance / 12
    upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    eps = 0.05
    
    while abs(balance) > eps:
        monthlyPayment = (lowerBound + upperBound) / 2
        balance = og_balance
        for i in range(12):
            monthlyUnpaidBalance = balance - monthlyPayment
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
        if balance > eps:
            lowerBound = monthlyPayment    
        elif balance < -eps:
            upperBound = monthlyPayment
        else:
            return round(monthlyPayment, 2)


print('Lowest Payment:', minFixedMonthlyPaymentBisection(320000, 0.2))