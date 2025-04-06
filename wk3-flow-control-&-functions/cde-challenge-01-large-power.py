#!/usr/bin/python3
import math

"""
    Create a method that tests whether the result of taking the power of one number to another
    number provides an answer which is greater than 500. We will use a conditional statement to 
    return True if the result is greater that 5000 or return False if it is not.
"""

def large_power(base, exponent):
    result = True if pow(base, exponent) > 5000 else False
    print(result)
    
print('Enter values to evaluate')

base = float(input("Enter base number:  "))
exponent = float(input("Enter the exponent: "))

large_power(base, exponent)