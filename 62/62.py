#!/usr/local/bin/python3
import itertools

class Record(object):
	def __init__(self, num):
		self.count = 0
		self.num = num

	def __str__(self):
		return '%d -- %d' % (self.num, self.count)

	def __add__(self, rhs):
		self.count += rhs
		return self

class CubeIterator(object):
	def __init__(self, target):
		self.seen_cubes = {}
		self.cube_gen = self.cubes_faster()
		self.target = target 

		self.prev_digits = 0

	def __iter__(self):
		return self

	def __next__(self):
		num = next(self.cube_gen)
		digits_num = map(int, str(num))
		base = tuple(sorted(digits_num))

		if (len(base) > self.prev_digits):
			self.prev_digits = len(base)
			result = self.raise_order()
			if result:	
				print(result)
				raise StopIteration

		self.seen_cubes[base] = self.seen_cubes.get(base, Record(num)) + 1

		return base

	def raise_order(self):
		for k,v in self.seen_cubes.items():
			if v.count == self.target:
				return v
		
		# clear the map when number of digits changes
		self.seen_cubes = {}
		return None

	def cubes_faster(self):
		odds = itertools.count(1, 2)

		for count in itertools.count(1):
			cube = 0
			for i in range(0,count):
				cube += next(odds)
			yield cube


cube_iter = CubeIterator(5)
for c in cube_iter:
	pass
