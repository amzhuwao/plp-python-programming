# Get a list of uppercase characters from a string Hello World
letters = [s.upper() for s in 'Hello World' if s != ' ']
print(letters)

# create a list of characters in apple, replacing non vowels with '*'
# Ex - 'apple' --> ['a', '*', '*', '*' ,'e']
apple = [x if x in 'aeiou' else '*' for x in 'apple']
print(apple)

# create a dictionary containing even numbers below 10 as the key and their square as the value
squares = {x: x**2 for x in range(1,10) if x % 2 == 0}
print(squares)