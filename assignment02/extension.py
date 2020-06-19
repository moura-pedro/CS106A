"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""


def main():
    num = float(input("Enter: "))
    num2 = 0
    while num >= num2:
        num2 = num
        num = float(input("Enter: "))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
