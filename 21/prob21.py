#!/usr/bin/python

# Class to memoize a function with an arbitrary number of non-mutable arguments
class Memoize:
	def __init__(self, fn):
		self.fn = fn
		self.memo = {}
	
	def __call__(self, *args):
		if not self.memo.has_key(args):
			self.memo[args] = self.fn(*args)
		return self.memo[args]

def d(n):
	dsum = 0
	for i in range(1,n):
		if n % i == 0:
			dsum = dsum + i
	return dsum
d = Memoize(d) # convert d into a memoized function

amicable = {}
def addtolist(n):
	if not amicable.has_key(n):
		amicable[n] = 1


for a in range(1,10000):
	b = d(a)
	if a != b and d(b) == a:
		addtolist(a)
		addtolist(b)

print sum(amicable.keys())
