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

def f(x,y,xmax,ymax,count):
	if (x > xmax or y > ymax):
		return 0
	elif (x == xmax and y == ymax):
		return 1 
	else:
		return f(x+1,y,xmax,ymax,1) + f(x,y+1,xmax,ymax,1)

f = Memoize(f) # convert f into a memoized function
def numberOfPaths(n):
	return f(0,0,n,n,0)


print numberOfPaths(20)
