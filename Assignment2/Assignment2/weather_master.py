"""
File: weather_master.py
Name: Robin Lee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


def main():
	"""
	TODO:to analyze temperature data ,and sort of highest、lowest and average
	"""
	tem = int(input('Next  temperature: (or -100 to quit)? '))
	n = 0
	sum = 0

	if tem == -100:   # if user don't enter any data, cause can't record any things

		print("No temperature data")
	else:
		highest = tem
		lowest = tem
		cold_day = 0

	while tem != -100:

		n += 1  # calculate how many times user enter number
		sum = sum + tem

		if tem > highest:
			highest = tem

		if tem < lowest:
			lowest = tem

		if tem < 10:
			cold_day += 1
		tem = int(input('Next temperature:(or -100 to quit)? '))

	avg = sum / n

	print('highest temperature: ', str(highest))
	print('lowest temperature: ', str(lowest))
	print('Average temperature: ', avg)
	print(cold_day, 'cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
