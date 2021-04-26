import random

Chance = 7

def main():
    my_random_word = random_word()
    dash_img = dash(my_random_word)
    chance = Chance

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
                    if dash_img[i].isalpha():
                        new_str += dash_img[i]
                    else:
                        new_str += '_'

            dash_img = new_str
            print('You are correct')

        else:
            chance -= 1
            print('There is no', guess, '\'s in the word')

        if dash_img == my_random_word:
            break

    if chance == 0:
        print("You are completely hung : (")
    else:
        print('You win')

    print('The word is : ' ,my_random_word)




def dash(my_random_word):
    dash = ''
    for i in range(len(my_random_word)):
        dash += '_'
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