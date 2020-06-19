from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    xablau()
"""
Makes Karel move from 1st avenue  to 9th,
also checking if will be needed to "climb a wall".
"""
def xablau():
    for i in range(8):
        climb()
    put_beeper()

def climb():
    if front_is_clear():
        m_b()
    else:
        turn_left()
        walk()
        jump()
        walk_back()

def walk(): # When it has a wall, makes Karel move all the way up
    while right_is_blocked():
        m_b()

def walk_back():    # Makes Karel move back to the 1st street
    while front_is_clear():
            m_b()
    turn_left()


def jump():     # line up for "walk_back()"
    turn_right()
    m_b()
    turn_right()
    m_b()

def m_b():  # move and put beepers along the path
    if no_beepers_present():
        put_beeper()
        move()
    elif beepers_present():
        move()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
