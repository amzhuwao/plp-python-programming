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
