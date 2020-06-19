from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
Makes Karel go outside of its house, pick up the
newspaper (represented by a beeper), and then return
to its initial position in the upper left corner of
the house.
"""


def main():
    collect()

def collect():
    move_to_door()
    pick_news()
    go_inside()

# pre: Karel is positioned in the upper left corner of the house
# post: karel still inside of its house, facing the door
def move_to_door():
    while front_is_clear():
        move()
    turn_right()
    while left_is_blocked():
        move()
    turn_left()

# pre: Karel must be facing the door
# post: Karel walks until see the beeper, and collect it
def pick_news():
    while no_beepers_present():
        move()
    pick_beeper()

# pre: Karel collected the beeper
# post: Karel turn around and returns to its initial position in the upper left corner of the house.
def go_inside():
    turn_around()
    for i in range(2):
        while front_is_clear():
            move()
        turn_right()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
