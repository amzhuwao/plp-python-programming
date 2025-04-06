#!/usr/bin/python3
import os

def modify_file(filename):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    input_file = os.path.join(script_dir, filename)
    output_file = os.path.join(script_dir, "output.txt")

    try:
        with open(input_file, "r") as file:
            data = file.read().upper()
            words = len(data.split())

        with open(output_file, "w") as file:
            file.write(f"{data}\nWord count is {words}")
            print("✅ File created successfully :)")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except IOError:
        print("❌ Error: Unable to read or write the file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Ask user for input filename
user_file = input("Enter the name of the file to read from (e.g., input.txt): ")

# Optional: Create a sample file if it doesn't exist (for testing/demo purposes)
sample_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), user_file)
if not os.path.exists(sample_path):
    with open(sample_path, "w") as f:
        f.write("1. Beautiful is better than ugly\n2. Explicit is better than implicit\n3. Simple is better than complex\n4. Complex is better than complicated\n5. Flat is better than nested")

modify_file(user_file)


