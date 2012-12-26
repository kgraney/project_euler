#!/bin/env python3
import copy

class Tile(object):
	def __init__(self):
		self.color = self.__class__.color
		self.size = self.__class__.size

	def __str__(self):
		return self.color * self.size

	@classmethod
	def get(cls):
		'''return a single object of each class type to avoid constructing
		many many objects'''
		return Tile.objects[cls]

class BlackTile(Tile):
	color = 'B'
	size = 1

class RedTile(Tile):
	color = 'r'
	size = 2

# tile choices are all sublcasses of Tile
tile_choices = sorted(Tile.__subclasses__(), key=lambda x: x.size)
Tile.objects = dict((cls, cls()) for cls in tile_choices)

class Model(object):
	def __init__(self, size):
		self.tiles = []
		self.size = size

	def __len__(self):
		return sum(x.size for x in self.tiles)

	def finished(self):
		return len(self) >= self.size

	def add(self, tile):
		if (tile.size + len(self)) > self.size:
			return False
		else:
			self.tiles.append(tile)
			return True

	def print_model(self):
		print(''.join([str(x) for x in self.tiles]))

models = [Model(20)]
while not all(x.finished() for x in models):
	for m in (x for x in models if not x.finished()):
		orig = copy.deepcopy(m)
		new_m = m
		new = False
		for tile in tile_choices:
			result = new_m.add(tile.get())
			if (result):
				if new:
					models.append(new_m)
				new_m = copy.deepcopy(orig)
				new = True
			else:
				break

for x in models:
	x.print_model()
