from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
Makes Karel paint the exterior of
three buildings in a given world.
"""

def main():
    for i in range(3):
        paint()

def paint():
    """
    Makes Karel paint 3 walls of a building
    and moves to another building.

    * Pre-condition: Karel has its left blocked by a wall of a building.

    * Post-condition: Karel painted(put beeper around) one of the buildings and moves to another building.
    """
    for i in range(3):
        corner()
        beepering()
    next()


def beepering():
    """
    Makes Karel move while its left side is block,
    dropping a beeper before each step it takes.

    * Pre-condition: Karel has its left side blocked.

    * Post-condition: Karel is facing the same direction as before, and
    after moving for every beeper added, its painted a wall of a building.
    """
    while left_is_blocked():
        put_beeper()
        move()

def corner():
    """
    Makes, if Karel's left side is clear,
    turn left and move one step, and now has
    its left blocked by a wall of a building.

    * Pre-condition: Karel is in one of the corners
    of the building, and has left side is clear.

    * Post-condition: Karel turns left, moves one step, NO beeper
    dropped, and now has its left blocked by a wall of the same building.
    """
    if left_is_clear():
        turn_left()
        move()

def next():
    """
    Makes Karel transition from a building
    to another by turning right.

    * Pre-condition: Karel has its front blocked and both left and right clear.

    * Post-condition: Karel turns right, now having its front clear
    and left side blocked by a wall from a NEW building.
    """
    if facing_east():
        turn_right()
    else:
        if facing_north():
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()