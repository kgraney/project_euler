#!/bin/env python3
from math import sqrt
from functools import total_ordering
from itertools import tee, combinations

def pairwise(iterable):
	"s -> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)


MAX_RNG = 10000

# use a sieve to get a list of all 4-digit primes
primes = list(range(1, MAX_RNG))
primes[0] = 0
factor = 2
while factor <= sqrt(MAX_RNG):
	index = factor
	while index < MAX_RNG - 1:
		primes[index - 1] = 0
		index += factor

	factor = next(p for p in primes if p > factor)

# store extra data with a number, so we can work on it
class Number:
	def __init__(self, value):
		self.value = value
		self.digits = tuple(map(int, str(value)))
		self.sdigits = tuple(sorted(self.digits))

	def __hash__(self):
		'''hash equal if all digits are equal'''
		return hash(self.sdigits)

	@total_ordering
	def __lt__(self, other):
		return self.value < other.value

	def __eq__(self, other):
		return self.value == other.value

	def __sub__(self, other):
		return self.value - other.value

	def __str__(self):
		return str(self.value)

# filter the sieve and convert all the ints to Number objects
primes = [Number(p) for p in primes if p != 0 and p >= 1000]

# group the Numbers by their hash (set of digits)
buckets = {}
for p in primes:
	try:
		buckets[hash(p)].append(p)
	except(KeyError):
		buckets[hash(p)] = [p]

# remove groups with too few items, sort those that remain
for k,v in list(buckets.items()):
	if len(buckets[k]) <= 2:
		del buckets[k]
	else:
		buckets[k] = sorted(buckets[k])

# return true if the list is an arithmetic sequence
def is_arithmetic(lst):
	return all(y-x == lst[1]-lst[0] for x,y in pairwise(lst))
	
# develop a list of all the candidate sequences
candidates = []
for k,v in list(buckets.items()):
	for l in range(3, len(v)):
		candidates.extend(combinations(v, l))

for l in candidates:
	if is_arithmetic(l):
		print(','.join(map(str, l)))

