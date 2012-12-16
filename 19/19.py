#!/usr/local/bin/python3
import itertools

months = [ 'January', 'February', 'March', 'April', 'May', 'June',
	'July', 'August', 'September', 'October', 'November', 'December']

month_lengths = {
	'January' : 31,
	'February' : 28,
	'March' : 31,
	'April' : 30,
	'May' : 31,
	'June' : 30,
	'July' : 31,
	'August' : 31,
	'September' : 30,
	'October' : 31,
	'November' : 30,
	'December' : 31,
}

class Year(object):
	def __init__(self, year):
		self.year = year

	def get_month_length(self, month):
		'''return the length of the given month'''
		length = month_lengths[month]
		if month != 'February':
			return length
		else:
			return length + self.leap_adjust()

	def leap_adjust(self):
		'''return the extra days in February for this year'''
		if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
			return 1
		else:
			return 0

def day_generator():
	days = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Tuesday']
	# start on Tuesday for January 1, 1901
	for d in itertools.cycle(days):
		yield d

count = 0
days = day_generator()
for yr_num in range(1901, 2001):
	year = Year(yr_num)
	for month in months:
		length = year.get_month_length(month)
		for day in range(1, length+1):
			day_name = next(days)
			#print('%s %d, %d -- %s' % (month, day, yr_num, day_name))
			if (day == 1 and day_name == 'Sunday'):
				count += 1

print(count)
