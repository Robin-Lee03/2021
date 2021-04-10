"""
File: quadratic_solver.py
Name: Robin Lee
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Hando
ut.
"""

import math


def main():
	"""
	This program should implement a equation
	ax^2 + bx + c = 0

	"""
	a = float(input("Enter a:"))
	b = float(input('Enter b:'))
	c = float(input('Enter c:'))
	d = float(b * b - (4 * a * c))  # discriminant

	if d > 0:
		d = math.sqrt(d)  # Do discriminant when discriminant >=0
		n1 = (-b - float(d)) / (2 * a)
		n2 = (-b + float(d)) / (2 * a)
		print('two roots:', str(n1), str(n2))
	elif d < 0:           # if discriminant > 0 don't have real roots
		print('No real roots')
	else:
		d = math.sqrt(d)  # Do discriminant when discriminant >=0
		n3 = (-b) / (2 * a)
		print('one roots' + str(n3))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
