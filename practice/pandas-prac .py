#!/usr/bin/python3
import pandas as pd

"""
📊 Practice Task (Pandas)
    Create a DataFrame with 3 students: name, age, and grade.

    Add a column called “Passed” where grade > 50 = True.

    Filter and display only students who passed.
"""
 
my_dataframe = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                             'Age': [24, 30, 22],
                             'Score': [85, 40, 95]
                             })

my_dataframe['passed'] = ['True' if x > 50  else 'False' for x in my_dataframe['Score']]


my_dataframe = my_dataframe[my_dataframe['passed'] == 'True']

print(my_dataframe)