#!/usr/bin/python

from decimal import *
import math

def choose(n, k):
	if 0 <= k <= n:
		p = 1
		for t in xrange(min(k, n - k)):
			p = (p * (n - t)) // (t + 1)
		return p
	else:
		return 0
def compute_raw(p,q,n):
	getcontext().prec=2*n + 10
	return getcontext().power(Decimal(p).sqrt() + Decimal(q).sqrt(), 2*n)

compute_memo = {}
def compute(p,q,n):
	getcontext().prec=2*n + 10
	getcontext().rounding=ROUND_DOWN

	if (compute_memo.has_key(tuple([p,q,n-1]))):
		print "map hit on: " + str(p) + " " + str(q) + " " + str(n-1)
		return compute_raw(p,q,1) * compute_memo[tuple([p,q,n-1])]

	k = 1
	value = 0
	sqrt_q_over_p = Decimal(float(q)/p).sqrt()
	power_term = sqrt_q_over_p 

	while (k <= 2*n):
		new_term = (choose(2*n,k) * power_term)
		#new_term = new_term - new_term.to_integral_exact()
		value = value + new_term
		value = value - value.to_integral_exact()
		power_term = power_term * sqrt_q_over_p * sqrt_q_over_p
		k = k + 2

	value = value * Decimal(p**n)
	compute_memo[tuple([p,q,n])] = value
	return value

def c2(p,q,n):
	getcontext().prec=2*n + 10
	getcontext().rounding=ROUND_DOWN
	value = -2*n*getcontext().log10(Decimal(p).sqrt() + Decimal(q).sqrt())
	print value

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
def c2(p,q,n):
	val = compute_raw(p,q,n)
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

#N(2,3)
print c2(2,3,1000)
