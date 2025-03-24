#Write a Python function that checks if a number is even or odd and prints the result. 
import random 
result = ""

def even_odd(number):
    if number % 2 == 0:
        print("The value " , number , " is even")
    else:
        print("The value " , number , " is odd")
    return(result)

even_odd(random.randint(1,12))

