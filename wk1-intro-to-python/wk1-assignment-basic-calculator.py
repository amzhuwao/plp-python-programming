"""
Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division)
Perform the operation based on the user's input and print the result.
Example: if a user inputs 10, 5, and +, your program should display 10 + 5 = 15
"""
import sys
    
try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")
    
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                sys.exit()
            result = num1 / num2
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
            sys.exit()
    
        print(f"Result: {result}")

except ValueError:
        print("Invalid input. Please enter numeric values.")
