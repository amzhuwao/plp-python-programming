import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
file_path = os.path.join(script_dir, "even-odd.py")

# Open the file
with open(file_path, "r") as file:
    print(file.read())

