#!/bin/env python3
import functools
import operator

@functools.total_ordering
class NineSeries(object):
	def __init__(self):
		self.gen = self.gen_func()
		self.current_value = 0
		self.length = 0
		next(self)
	
	# The generator function
	def gen_func(self):
		n = 1
		p = 1
		while True:
			yield n*9
			n += 10**p
			p += 1

	def __next__(self):
		self.current_value = next(self.gen)	
		self.length += 1
		return self.gen

	# Comparison operators are all defined in terms of current_value
	def __eq__(self, other):
		return (self.current_value == other.current_value)

	def __lt__(self, other):
		return (self.current_value < other.current_value)

	# Need the modulo operator for below algorithm (it would be nice if
	# something like total_ordering existed to define all of these to
	# operate on self.current_value)
	def __mod__(self, rhs):
		return self.current_value % rhs

	def __str__(self):
		return str(self.current_value)

def cycle_length(d):
	M = d
	while (M % 2 == 0):
		M //= 2
	while (M % 5 == 0):
		M //= 5

	if M == 1:
		# non-repeating decimal
		return 0

	nine_num = NineSeries()
	while nine_num % M != 0:
		next(nine_num)

	return nine_num.length

tuples = ((d, cycle_length(d)) for d in range(1,1000))

highest = max(tuples, key=lambda x: x[1])
print(highest[0])
