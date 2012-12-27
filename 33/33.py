#!/bin/env python3
from functools import reduce
from operator import mul

class Fraction:
	def __init__(self, num, den):
		self.flt = num/den
		self.num = num
		self.den = den

		self.num_digits = [num // 10, num % 10]
		self.den_digits = [den // 10, den % 10]

	def reduce(self):
		nd = sorted(self.num_digits)
		dd = sorted(self.den_digits)

		new_nd = []
		new_dd = []
		while (len(nd) > 0 and len(dd) > 0):
			if nd[0] == dd[0]:
				nd.pop(0)
				dd.pop(0)
			else:
				if nd[0] > dd[0]:
					new_dd.append(dd.pop(0))
				else:
					new_nd.append(nd.pop(0))

		new_dd.extend(dd)
		new_nd.extend(nd)

		if len(new_nd) == 1 and len(new_dd) == 1:
			if new_dd[0] != 0:
				return Fraction(new_nd[0], new_dd[0])
			else:
				return None
		else:
			return None

	def __mul__(self, other):
		return Fraction(self.num * other.num, self.den * other.den)

	def __eq__(self, other):
		return self.flt == other.flt

	def __str__(self):
		return '%d/%d' % (self.num, self.den)



fracs = []
for num in range(10,100):
	for den in range(num + 1,100):
		f = Fraction(num, den)
		reduced = f.reduce()
		if (reduced and f == reduced):
			if (f.num % 10 != 0): # eliminate "trivial" ones
				fracs.append(reduced)
				print(f, reduced)

print()
result = reduce(mul, fracs)
print(result)
