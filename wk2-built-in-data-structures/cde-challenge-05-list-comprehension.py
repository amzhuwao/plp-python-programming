#1/usr/bin/python3
"""
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains 
only the words that have an odd number of characters.
"""
print('Enter any 5 words')
count = 0
list1 = []

while count < 5:
    list1.append(input('Please enter the next word\n'))
    count+= 1

    
list2 = [x for x in list1 if len(x) % 2 != 0]

print(list2)


