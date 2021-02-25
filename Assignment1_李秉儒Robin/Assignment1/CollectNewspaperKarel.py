from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    TODO:Karel need to go to find beeper and pick it up and turn back

    """
    move_to_deeper()
    turn_back()


def turn_back():
    """
    pre-condition: Karel has found beeper and standing on beeper facing east
    post-condition: Karel at the (4,3) facing east but standing on beeper


    """
   
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        turn_right()
        move()
        turn_left()
    if not right_is_clear():
        move()
        move()
        turn_around()
        put_beeper()


def move_to_deeper():
    """
    pre-condition: Karel at the (4,3) facing east
    post-condition:Karel has found beeper and standing on beeper facing east


    """

    while front_is_clear():
        move()
    if not front_is_clear():
      turn_right()
      move()
      turn_left()
      move()



def turn_right():
    for x in range(3):
        turn_left()


def turn_around():
    for a in range(2):
        turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
