#!/usr/bin/python3
import numpy as np

"""
🎲 Practice Task (NumPy)
    Create an array with numbers 10 to 50.

    Find the maximum and minimum values.

    Multiply all elements by 3.
"""
 
my_array = np.array([x for x in range(10, 50)])

print(f'Maximum value is : {np.max(my_array)}')

print(f'Minimum value is : {np.min(my_array)}')

print(f'Multiple by 3 : {my_array * 3}')