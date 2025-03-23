"""
    Create a multiple choice quize with question about Python, movies, or any 
    fun topic! Display scores at the end and allow the user to play again.
"""
while True:
    print("Welcome to the Quiz. ")

    name = input("Please enter your name...")
    score = count = 0

    questions = {
        'What is the print function in Python used for?' : [
                                                            'A) To store data in a variable',
                                                            'B) To perform arithmetic operations',
                                                            'C) To output text to the screen',
                                                            'D) To import modules'],

        'What is the difference between the `==` and `is` operators in Python?' : [
                                                            'A) `==` checks for equality, while `is` checks for identity',
                                                            'B) `==` checks for identity, while `is` checks for equality',
                                                            'C) `==` is used for numbers, while `is` is used for strings',
                                                            'D) `==` is used for strings, while `is` is used for numbers'],

        'What is the purpose of the `if __name__ == "__main__":` block in Python?' : [
                                                            'A) To define a function',
                                                            'B) To import a module',
                                                            'C) To ensure the code is executed only when the script is run directly',
                                                            'D) To create a class'],

        'What is the difference between a list and a tuple in Python?' : [
                                                            'A) Lists are immutable, while tuples are mutable',
                                                            'B) Tuples are immutable, while lists are mutable',
                                                            'C) Lists are used for numbers, while tuples are used for strings',
                                                            'D) Tuples are used for numbers, while lists are used for strings'],

        'What is the purpose of the `try`-`except` block in Python?' : [
                                                            'A) To handle errors and exceptions',
                                                            'B) To define a function',
                                                            'C) To import a module',
                                                            'D) To create a class'],

        'What is the difference between the `break` and `continue` statements in Python?' : [
                                                            'A) `break` exits the loop, while `continue` skips to the next iteration',
                                                            'B) `continue` exits the loop, while `break` skips to the next iteration',
                                                            'C) `break` is used for `for` loops, while `continue` is used for `while` loops',
                                                            'D) `continue` is used for `for` loops, while `break` is used for `while` loops'],                                          

        'What is the purpose of the `import` statement in Python?' : [
                                                            'A) To define a function',
                                                            'B) To import a module',
                                                            'C) To create a class',
                                                            'D) To handle errors and exceptions'],

        'What is the difference between a dictionary and a set in Python?' : [
                                                            'A) Dictionaries are mutable, while sets are immutable',
                                                            'B) Sets are mutable, while dictionaries are immutable',
                                                            'C) Dictionaries are used for key-value pairs, while sets are used for unique elements',
                                                            'D) Sets are used for key-value pairs, while dictionaries are used for unique elements'],

        'What is the purpose of the `lambda` function in Python?' : [
                                                            'A) To define a regular function',
                                                            'B) To create a class',
                                                            'C) To import a module',
                                                            'D) To define a small, anonymous function'],

        'What is the difference between the `zip` and `enumerate` functions in Python?' : [
                                    'A) `zip` is used to iterate over two lists, while `enumerate` is used to iterate over a list with indices',
                                    'B) `enumerate` is used to iterate over two lists, while `zip` is used to iterate over a list with indices',
                                    'C) `zip` is used to iterate over a list with indices, while `enumerate` is used to iterate over two lists',
                                    'D) `enumerate` is used to iterate over a list with indices, while `zip` is used to combine two lists into a dictionary']
    }

    answers = ['c', 'a', 'c', 'b', 'a', 'a', 'b', 'c', 'd', 'a']

    for i in questions.keys():
        print(f'\n{i}')

        for j in range(0,4):
            print(questions[i][j])

        usr_answer = input("...")

        if usr_answer == answers[count]:
            score+=1

        count+=1
            
    print(f'{name}, you scored {score}')

    retake = input("Would you like to play again?(y/n)...")

    if retake == "n" or retake == "N":
        print('Bye')
        break
    else:
        print()

