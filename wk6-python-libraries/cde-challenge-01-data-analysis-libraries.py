#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib as plt
import os

"""
📌 Task Requirements:
    Import the following libraries:
        pandas (for data manipulation)
        numpy (for numerical operations)
        matplotlib (for data visualization)
        requests (for making web requests)
    
    Complete the following tasks using the libraries:
        Create a NumPy array of numbers from 1 to 10 and calculate the mean.
        Load a small dataset into a pandas DataFrame and display summary statistics.
        Fetch data from a public API using requests and print a key piece of information.
        Plot a simple line graph using matplotlib (e.g., a list of numbers).
"""
# Create a NumPy array of numbers from 1 to 10 and calculate the mean.
my_array = np.array([x for x in range(1, 10)])
mean = np.mean(my_array)
print(f'My Array: {my_array}\nMean: {mean}\n')


# Load a small dataset into a pandas DataFrame and display summary statistics.

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
file_path = os.path.join(script_dir, "iris.csv")

iris_data = pd.read_csv(file_path )
print(f'My Iris Data:\n {iris_data.head(10)}')
print(f'Sepal length Mean: {iris_data['sepal_length'].mean()}')
print(f'Max Petal length: {iris_data['petal_length'].max()}')
print(f'setosa: {iris_data['species'].count()}')


# Fetch data from a public API using requests and print a key piece of information.


# Plot a simple line graph using matplotlib (e.g., a list of numbers).

    
    