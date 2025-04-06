#!/usr/bin/python3


"""
    Create a function that determines whether or not a number is divisible bt ten.
"""

def divisible_by_ten(num):
    result = True if num % 10 == 0 else False
    print(result)
    

print('Enter number to evaluate')
divisible_by_ten(num = float(input("Enter base number:  ")))