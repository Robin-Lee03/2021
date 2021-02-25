from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    pre-condition: Karel at the 1-1 facing East,each column need beeper to fill up
    post-condition:every column have deeper and Karel is at the lower-right corner and facing east
    """
    if not on_beeper():
        put_beeper()

    while left_is_clear():

        go_up_put()
        go_down()
        go_straight()
        if not front_is_clear():

            if not right_is_clear():
                go_up_put()
                go_down()
                pick_beeper()
                while not front_is_clear():
                    if not on_beeper():
                        pass


def go_up_put():
    """
    pre-condition: Karel at the first floor facing east
    post-condition:Karel at the top floor standing on the beeper facing south


    """

    if left_is_clear():
        turn_left()
        if not on_beeper():             #最後行第1個沒有beeper的話要先放
            put_beeper()

    while front_is_clear():
        move()
        if not on_beeper():
            put_beeper()
    while not front_is_clear():
        turn_around()


def go_down():
    """
        pre-condition: Karel at the top floor standing on the beeper facing south
        post-condition:Karel at the first floor standing on the beeper facing east
    """


    while front_is_clear():
        move()
    if not front_is_clear():
        turn_left()         #Karel在最底端 面向東邊


def go_straight():
    """
            pre-condition: Karel at the first floor standing on the beeper facing east
            post-condition: Karel under the next column of first floor
    """

    if front_is_clear():
        for x in range(4):
            move()


def turn_around():
    for a in range(2):
        turn_left()


def turn_right():
    for r in range(3):
        turn_left()








# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
