from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

def main():
    repair()

def repair():
    """
    Makes Karel fill a column from bottom to top
    and then go back to the wall which it started filling.

    * Pre-condition:
    """

    turn_left()
    check()

    while front_is_clear():
        fill()
    move_to_wall()

def fill():
    check()
    move()
    check()

def check():
    if no_beepers_present():
        put_beeper()

# go back to the wall and call "next" func
def move_to_wall():
    turn_around()
    while front_is_clear():
        move()
    next()

# move to the next column and calls fill() func
def next():
    turn_left()
    if front_is_clear():
        for i in range(4):
            move()
        repair()

# 180º turn
def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
