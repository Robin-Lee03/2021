from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Jenny revised one
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""




def main():
    """
    pre-condition: Karel at the (1,1) facing East,amd no beeper on the map
    post-condition:here must be a space in the middle of each beeper on the whole of map
    """
    put_beeper()

    while front_is_clear():
        layout_east()
        layout_west()

    while not front_is_clear():
        """
            pre-condition: Karel at the (1,1) facing East, the wall is front of Karel
            
            post-condition:Karel is facing west,not on beeper at (8,1)
        """

        layout_north()


def layout_north():
    while facing_east():
        turn_left()
    while facing_north():
        if on_beeper():
            move()
            if not on_beeper():
                if front_is_clear():
                    move()
                    put_beeper()
                else:
                    turn_left()


def layout_west():
    """
    pre-condition: Karel is front of east wall , facing west
    post-condition:Karel is front of west wall and standing on beeper facing east
    """
    while facing_west():
        if front_is_clear():
            if on_beeper():
                move()
            else:
                if front_is_clear():
                    move()
                    put_beeper()
        else:  # 左邊撞牆時
            if not on_beeper():  # 左邊撞牆要往上時一定是沒有beeper
                turn_right()
                if front_is_clear():  # karel面對北方，可以往前時才往前 （到左上角會停住）
                    move()
                    put_beeper()
                    turn_right()


def layout_east():
    """
        pre-condition: Karel is front of west wall and standing on beeper facing east
        post-condition: Karel is front of east wall , facing west
    """

    while facing_east():
        if front_is_clear():
            if on_beeper():
                move()
            else:
                if front_is_clear():
                    move()
                    put_beeper()
        else:                 # 右邊撞牆時
            if not on_beeper():  # 右邊撞牆要往上時一定是沒有beeper
                turn_left()
            else:
                turn_left()
            if front_is_clear(): # karel面對北方，可以往前時才往前
                if on_beeper():
                    move()
                    turn_left()
                else:
                    move()
                    turn_left()
                    put_beeper()



def turn_around():
    for k in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)







