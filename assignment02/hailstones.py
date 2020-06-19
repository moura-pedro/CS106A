"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    steps = 0
    number = int(input("Enter a number: "))

    while number < 1:
        number = int(input("Please, enter a positive number: "))

    while number > 1:
        # check if the number is even or odd
        if number % 2 == 0:
            even = number / 2
            print(f"{number} is even, so I take half: {int(even)}")
            number = even    # make number an integer, again
            steps += 1
        else:
            odd = (3 * number) + 1
            print(f"{number} is odd, so I make 3n + 1: {int(odd)}")
            number = odd
            steps += 1
    print(f"The process took {steps} to reach 1")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
