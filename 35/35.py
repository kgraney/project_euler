#!/bin/env python3
import numpy as np
from collections import deque

def digits(n):
	return list(map(int, str(n)))

def number(t):
	return int(''.join(map(str,t)))

def rotations(t):
	q = deque(t)
	def rotate():	
		q.rotate(1)
		return tuple(q)

	return (rotate() for n in range(0,len(t)))

max_val = 1000000

sieve = np.ones(max_val, dtype=bool)
sieve[0:2] = False # mark zero and one as non-prime
for i in range(2,max_val): # begin elimination at 2
	if sieve[i] == True:
		for j in range(2*i,max_val,i):
			sieve[j] = False

primes = np.nonzero(sieve)[0]
zeros = np.zeros(primes.size, dtype=bool)

prime_set = dict(zip(primes, zeros))


circulars = set()
for p in primes:
	if prime_set[p] == False:
		prime_set[p] = True

		circular = True
		local_circulars = [p]
		for perm in map(number, rotations(digits(p))):
			if perm in prime_set:
				local_circulars.append(perm)
			else:
				circular = False
				break

		if circular:
			for perm in local_circulars:
				prime_set[perm] = True
			circulars |= set(local_circulars)

print(circulars)
print(len(circulars))
