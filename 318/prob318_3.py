#!/usr/bin/python

from decimal import *
import math

def c2(p,q,n):
	getcontext().prec=2*n+100
	getcontext().rounding=ROUND_DOWN

	#value = 2*n*getcontext().log10(Decimal(p).sqrt() + Decimal(q).sqrt())

	squared = p + 2*Decimal(p*q).sqrt() + q
	#squared = getcontext().power(squared,n)
	fractional = squared - squared.to_integral_exact()
	value = -n*getcontext().log10(1 - fractional)
	return value.to_integral_exact()

def gen_pq_pairs(max_sum):
	pairs = []
	for p in range(0,max_sum):
		for q in range(p+1,max_sum - p):
			pair = [p, q]
			pairs.append(pair)
	return pairs

#N(2,3)
#print c2(2,3,2020)
#gen_pq_pairs(2011)
print c2(2,3,1)
print c2(2,3,2)
print c2(2,3,3)
print c2(2,3,4)
