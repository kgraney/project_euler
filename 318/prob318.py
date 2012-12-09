#!/usr/bin/python

from decimal import *
import math

# Class to memoize a function with an arbitrary number of non-mutable arguments
class Memoize:
	def __init__(self, fn):
		self.fn = fn
		self.memo = {}
	
	def __call__(self, *args):
		if not self.memo.has_key(args):
			self.memo[args] = self.fn(*args)
		return self.memo[args]

def raw_compute(p,q,n):
	getcontext().prec=2*n + 100
	return getcontext().power(Decimal(p).sqrt() + Decimal(q).sqrt(), 2*n)

# returns the value of (sqrt(p) + sqrt(q))^(2n)
def compute(p,q,n):
	getcontext().prec=2*n + 100

	if (n <= 3):
		return getcontext().power(Decimal(p).sqrt() + Decimal(q).sqrt(), 2*n)
	else:
		return getcontext().multiply(compute(p,q,n-1), compute(p,q,1))

compute = Memoize(compute)

# returns the number of nines in a value (must be a Decimal object)
def count_nines(value):
	getcontext().rounding=ROUND_DOWN
	value = value - value.to_integral_exact()

	count = 0
	while (value.compare(Decimal('0.9')) >= 0):
		value = value.shift(1)
		value = value - 9
		count = count + 1
	return count

def c(p,q,n):
	val = compute(p,q,n)
	print val
	return count_nines(val)

def N(p,q):
	n =10  
	val = 0
	while (val < 2011):
		val = c(p,q,n)
		print "c(" + str(p) + "," + str(q) + "," + str(n) + ") = " \
			+ str(val) 
		n = n + 1
	print n

def N2(p,q):
	baseprec = 4
	getcontext().prec = baseprec
	base = getcontext().power(Decimal(p).sqrt() + Decimal(q).sqrt(), 2)

	n = 1
	getcontext().prec = 100
	value = getcontext().power(Decimal(p).sqrt() + Decimal(q).sqrt(), 2)
	number_of_nines = count_nines(value)

	while (number_of_nines <= 2011):
		getcontext().prec = int(value.log10())+ n + 10

		if (getcontext().prec >= baseprec):
			oldprec = getcontext().prec
			getcontext().prec = int(oldprec * 1.5 )
			baseprec = getcontext().prec
			print "recomputing base (precision = " + str(baseprec) + ")"
			base = getcontext().power(Decimal(p).sqrt() + Decimal(q).sqrt(), 2)
			getcontext().prec = oldprec

		prec = getcontext().prec

		n = n+1
		value = getcontext().multiply(value,base)
		number_of_nines = count_nines(value)
		print "value = " + str(value)
		print "n = " + str(n) + "  nines = " + str(number_of_nines)
		print "prec = " + str(prec) + "  baseprec = " + str(baseprec)
	return n

print N2(2,3)
#print compute(2,3,2000)
#print raw_compute(2,3,2000)
#print c(2,3,10)
