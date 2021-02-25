from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""





def main():
    """
    TODO:Karel need to find a midpoint and put beeper on midpoint
    """
    put_beeper()
    go_measure()
    back()
    turn_around()
    move_to_mid()


def move_to_mid():
    """
        pre-condition: Karel is front of the east/west wall depending on  the map is odd or even
        post-condition: Karel is standing on the midpoint meanwhile on the beeper

    """
    while not on_beeper():
        move()
        if on_beeper():

            pick_beeper()



def go_measure():
    """
    pre-condition: Karel on the (1.1) facing east on beeper
    post-condition: Karel is front of east hall and on beeper facing east

    """

    while front_is_clear():
        move()
        if not front_is_clear():
            put_beeper()


def back():
    """
       pre-condition:
       post-condition: Karel on the (1.1) facing west not on beeper

    """
    while not front_is_clear():
        if on_beeper():
            turn_around()
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_around()
            move()
            put_beeper()


def turn_around():
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()
# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
