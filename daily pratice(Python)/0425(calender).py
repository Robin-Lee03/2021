import calendar
import time


yy = int(input('Enter a year: '))
mm = int(input('Enter a month: '))
print(calendar.month(yy,mm))
print(time.localtime())
#
# date = str(input('Enter your birthday (ex:1998/01/05) :  '))
# result = date.split('/')


# print(calendar.TextCalendar(firstweekday=7).formatyear(2021))