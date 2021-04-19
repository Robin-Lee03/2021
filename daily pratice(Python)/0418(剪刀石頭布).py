from random import randint



choice = ['paper','scissors','stone']


def main():
    computer = choice[randint(0,2)]
    print('Welcome to the Game, you have to choice one from paper scissors stone')
    player = str(input('Enter your choices: ')).lower()

    print('Computer :', computer)
    if computer == player:
        print('Draw')
    elif player == 'paper' and computer == 'stone':
        print('You Win~!')
    elif player == 'scissors' and computer == 'paper':
        print('You Win~!')
    elif player == 'stone' and computer == 'scissors':
        print('You Win~!')
    else:
        print('You lose')







if __name__ == '__main__':
	main()