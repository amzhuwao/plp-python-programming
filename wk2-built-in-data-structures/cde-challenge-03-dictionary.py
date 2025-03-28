#!usr/bin/python3
"""
Write a program that uses a dictionary to store information about a person, such as their name, age, 
and favourite color. Ask the user for input and store the information in the dictionary. Then, print 
the dictionary to the console. 
"""

person = {}

person['name' ] = input('Please enter your name')
person['age'] = int(input('Please enter your age'))
person['fav_color'] = input('Please enter your favourite colour')

for i,j in person.items():
    print(f'{i}: {j}')