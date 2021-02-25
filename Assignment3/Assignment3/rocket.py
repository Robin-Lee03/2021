"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():

	for i in range(1):
		head()
		belt()
	# upper()
	# lower()
	# belt()
	# head()


def head():
	for i in range(3):
		print('/\\  ')


def belt():
	print('+',end='')
	for i in range(6):
		print('=',end='')
	print('+')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()