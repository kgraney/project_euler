#!/bin/python
import functools

def triangle():
	n = 285
	while True:
		yield n*(n+1)/2
		n += 1

def pentagonal():
	n = 165
	while True:
		yield n*(3*n-1)/2
		n += 1

def hexagonal():	
	n = 143
	while True:
		yield n*(2*n-1)
		n += 1

@functools.total_ordering
class GenSeries(object):
	def __init__(self, gen):
		self.gen = gen
		self.advance() # initial value

	def advance(self):
		self.curr_val = self.gen.next()

	# comparators based on current value
	def __eq__(self, other):
		return (self.curr_val == other.curr_val)

	def __lt__(self, other):
		return (self.curr_val < other.curr_val)

generators = [GenSeries(triangle()),
	GenSeries(pentagonal()),
	GenSeries(hexagonal())]

min(generators).advance() # advance beyond initial values

# advance lowest valued generator until they're all equal
while not all(x == generators[0] for x in generators):
	min(generators).advance()

print(generators[0].curr_val)
