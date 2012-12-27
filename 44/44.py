#!/bin/env python3
from itertools import tee

def max_default(iterable, default):
	try:
		return max(iterable)
	except(ValueError):
		return default

def pentagonal():
	n = 1
	while True:
		yield n*(3*n-1)/2
		n += 1

pentagonals = set()
p_gen = tee(pentagonal(), 2)

def advance(new_max):
	while max_default(pentagonals, 0) < new_max:
		pentagonals.add(next(p_gen[0]))

while True:
	num = next(p_gen[1])
	advance(num + max_default(pentagonals, 0))

	for candidate in pentagonals:
		summ = num + candidate
		diff = abs(num-candidate)
		if summ in pentagonals and diff in pentagonals:
			print(diff, (candidate, num))
			exit(0)

	pentagonals.add(num)

