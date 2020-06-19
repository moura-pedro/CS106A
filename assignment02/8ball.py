"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""
import random

MIN_ANSWER = 1
MAX_ANSWER = 20

def main():
    while question() != "":
        create_random_answer()

def question():
    ask = input("Ask a yes or no question: ")
    return ask

def create_random_answer():
    num = random.randint(MIN_ANSWER, MAX_ANSWER)
    check(num)

def check(value):
    if value == 1:
        print("As I see it, yes.")
    elif value == 2:
        print("Ask again later.")
    elif value == 3:
        print("Better not tell you now.")
    elif value == 4:
        print("Cannot predict now.")
    elif value == 5:
        print("Concentrate and ask again.")
    elif value == 6:
        print("Don’t count on it.")
    elif value == 7:
        print("It is certain.")
    elif value == 8:
        print("It is decidedly so.")
    elif value == 9:
        print("Most likely.")
    elif value == 10:
        print("My reply is no.")
    elif value == 11:
        print("My sources say no.")
    elif value == 12:
        print("Outlook not so good.")
    elif value == 13:
        print("Outlook good.")
    elif value == 14:
        print("Reply hazy, try again.")
    elif value == 15:
        print("Signs point to yes.")
    elif value == 16:
        print("Very doubtful.")
    elif value == 17:
        print("Without a doubt.")
    elif value == 18:
        print("Yes.")
    elif value == 19:
        print("Yes – definitely.")
    else:
        print("You may rely on it")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()