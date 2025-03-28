#1/usr/bin/python3
"""
Write a program that accepts user input to create two sets of integers, then create
a new set that contains only the elements that are common to both sets.
"""
print('Enter the values for the first set')
count = 0
set1, set2, set3 = [],[],[]

while count < 5:
    set1.append(int(input('Please enter an integer')))
    count+= 1
set1 = set(set1)

print('Enter the values for the secound set')
count = 0


while count < 5:
    set2.append(int(input('Please enter an integer')))
    count+= 1
set2 = set(set2)
    
set3 = set(set1 & set2)

print(set3)