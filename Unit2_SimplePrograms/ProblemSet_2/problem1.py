# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:36:36 2021

@author: ENkanga
"""

'''
Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. 
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print
Remaining balance: 813.41

instead of
Remaining balance: 813.4141998135 

So your program only prints out one thing: 
the remaining balance at the end of the year in the format:
Remaining balance: 4784.0

A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

def creditBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Calculates the credit card balance after one year 
    when paying only the minimum monthly payment.
    
    Parameters
    ----------
    balance : float
        the outstanding balance on the credit card.
    annualInterestRate : float
        annual interest rate.
    monthlyPaymentRate : float
        minimum monthly payment rate.

    Returns
    -------
    balance : float
        remaining credit card balance after one year

    '''
    monthlyInterestRate = annualInterestRate / 12.0
    for i in range(12):
        minMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return round(balance, 2)

print('Remaining balance:', creditBalance(42, 0.2, 0.04))