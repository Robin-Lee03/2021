"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    my_random_word = random_word()
    dash_img = dash(my_random_word)
    chance = N_TURNS

    while chance > 0:
        print("You have ", chance, " guesses left.")
        print('The word looks like: ', dash_img)
        guess = input("Your guess: ").upper()
        if not guess.isalpha() or len(guess) > 1:
            print('illegal format')

        elif guess in my_random_word:

            new_str = ''
            for i in range(len(my_random_word)):
                if guess == my_random_word[i]:
                    new_str += guess

                else:
                    if dash_img[i].isalpha():  # if last round user guess right alphabet,
                        new_str += dash_img[i]  # the '-' in dash_img will become truly alphabet
                    else:
                        new_str += '-'

            dash_img = new_str  # ensure every round the correct guess will be remain
            print('you are correct!')

        else:  # if user's guess not in the random_word the chance will -1
            chance -= 1
            print('There is no', guess, '\'s in the word')

        if dash_img == my_random_word:
            break

    if chance == 0:
        print("You are completely hung : (")
    else:
        print('You win ')

    print("The word was: ", my_random_word)


def dash(my_random_word):
    dash = ''
    for i in range(len(my_random_word)):
        dash += '-'

    return dash


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
