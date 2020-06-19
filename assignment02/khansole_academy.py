"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

GOAL = 3

def main():
    correct = 1

    while (correct <= GOAL):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        answer = num1 + num2

        print(f"What is {num1} + {num2}?")
        user_answer = int(input("Your answer: "))

        if (user_answer == answer):
            print(f"Correct! You've gotten {correct} in a row.")
            correct += 1
        else:
            print(f"Incorrect. The expected answer is {answer}")
            correct = 1

    print("Congratulations! You've achieved your goal!")
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
