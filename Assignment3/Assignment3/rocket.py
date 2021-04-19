"""
File: rocket.py
Name:Robin Lee
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

	head()
	belt()
	upper()
	lower()
	belt()
	head()


def lower():
	lower_img = ''
	for i in range(1,SIZE+1):            # because the later one(y) in range(x,y) exclude Maximun
		for j in range(1):
			lower_img += '|'
		for j in range(i-1):
			lower_img += '.'
		for j in range(i,SIZE+1):
			lower_img += '\\/'
		for j in range(i-1):
			lower_img += '.'
		for j in range(1):
			lower_img += '|'
		if i != SIZE:
			lower_img += '\n'

	print(lower_img)


def upper():
	upper_img = ''
	for i in range(1,SIZE + 1):
		for j in range(1):
			upper_img += '|'
		for j in range(SIZE - i):
			upper_img += '.'
		for j in range(i):
			upper_img += '/\\'
		for j in range(SIZE - i):
			upper_img += '.'
		for j in range(1):
			upper_img += '|'
		if i != SIZE:
			upper_img += '\n'
		else:
			break

	print(upper_img)


def head():
	head_img = ''
	for i in range(1, SIZE + 1):
		for j in range(i,SIZE+1):
			head_img += ' '
		for j in range(i):
			head_img += '/'
		for j in range(i):
			head_img += '\\'
		if i != SIZE:
			head_img += '\n'

	print(head_img)


def belt():
	belt_img = ''
	belt_img += '+'
	for i in range(SIZE+SIZE):
		belt_img += '='
	belt_img += '+'
	print(belt_img)



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()