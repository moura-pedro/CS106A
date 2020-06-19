from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    edges()
    verify()

def edges():
    # pre: Karel is on left bottom and faces East
    # pro: Karel put a beeper on 1x1 and moved to the last avenue at the same street and put a beeper
    put_beeper()
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

def verify():
    turn_around()
    if front_is_clear():
        move()
        if no_beepers_present():
            seek()
        else:
            turn_around()
            move()
            pick_beeper()
            turn_around()
            move()

    else:
        turn_around()

def seek():
    find_beeper()
    beeper_found()
    check()

def find_beeper():
    while no_beepers_present():
        move()

def beeper_found():
    if beepers_present():
        pick_beeper()
        turn_around()
        move()
        if no_beepers_present():
            put_beeper()
            move()

def check():
    if beepers_present():
        if facing_east():
            is_odd()
        else:
            if facing_west():
                is_even()
    else:
        seek()

def is_odd():
    pick_beeper()
    turn_around()
    move()

def is_even():
    turn_around()
    move()
    pick_beeper()
    turn_around()
    move()

def turn_around():
    for i in range(2):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()