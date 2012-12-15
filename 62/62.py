#!/usr/local/bin/python3
import itertools

class LookAheadGenerator(object):
	def __init__(self, gen):
		self.gen = gen
		self.buffer = []

	def __next__(self):
		if self.buffer:
			return self.buffer.pop(0)
		else:
			return next(self.gen)

	def lookahead(self, n=0):
		while n >= len(self.buffer):
			try:
				self.buffer.append(next(self.gen))
			except StopIteration:
				return []
		return self.buffer[n]

class CubeIterator(object):
	def __init__(self):
		self.seen_cubes = set()

		tee = itertools.tee(self.cubes_faster(), 2)

		self.cube_gen = tee[0]
		self.cache_gen = LookAheadGenerator(tee[1])

		self.last_computed = None
		self.cache_length = 0

	def __iter__(self):
		return self

	def __next__(self):
		num = next(self.cube_gen)
		self.advance_seen(len(num))
		return num

	def is_cube(self, val):
		return val in self.seen_cubes

	def cubes(self):
		for i in itertools.count(0):
			yield tuple(map(int, str(i**3)))

	def cubes_faster(self):
		odds = itertools.count(1, 2)

		for count in itertools.count(1):
			cube = 0
			for i in range(0,count):
				cube += next(odds)
			yield tuple(map(int, str(cube)))

	def advance_seen(self, length):
		if (self.cache_length >= length):
			return

		self.seen_cubes = set()
		while (len(self.cache_gen.lookahead()) <= length):
			self.seen_cubes.add(next(self.cache_gen))

		self.cache_length = length

cube_iter = CubeIterator()
for cube in cube_iter:
	perms = itertools.permutations(cube)
	#num_perms = [cube_iter.is_cube(p) for p in perms].count(True)

	counted_perms = set()
	for p in perms:
		if (cube_iter.is_cube(p) and not p in counted_perms):
			counted_perms.add(p)

		if len(counted_perms) > 5:
			break

	if (len(counted_perms) == 5):
		print(cube)
		break

