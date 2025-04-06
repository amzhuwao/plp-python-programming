#!/usr/bin/python3
import os

"""
Create a program that reads a text file, processes its content and writes the results to a new file
"""
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
input_file = os.path.join(script_dir, "input.txt")
output_file = os.path.join(script_dir, "output.txt")

# Create the file
with open(input_file, "w") as file: 
    file.write("1. Beautiful is better than ugly\n 2. Explicit is better than implicit\n 3. Simple is better than complex\n 4. Complex is better than complicated\n 5. Flat is better than nested")

# Create the file
with open(input_file, "r") as file: 
    data = file.read().upper()
    words = len(data.split())
    
with open(output_file, "w") as file:
    file.write(f"{data} \nWord count is {words}")
    print("File created successfully :)")
    
    