#!/bin/env python3
import copy
import sys

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
	color = 'R'
	size = 2

class GreenTile(Tile):
	color = 'G'
	size = 3

class BlueTile(Tile):
	color = 'L'
	size = 4

# tile choices are all sublcasses of Tile
tile_choices = sorted(Tile.__subclasses__(), key=lambda x: x.size)
Tile.objects = dict((cls, cls()) for cls in tile_choices)

length_map = {}
count_map = {}

GOAL_SIZE = int(sys.argv[1])
class TileNode(object):
	def __init__(self, tile, length=0):
		self.tile = tile
		self.children = []
		self.length = length

	def finished(self):
		return self.length >= GOAL_SIZE

	def add_child(self, child):
		new_length = self.length + child.size
		if new_length <= GOAL_SIZE:
			try:
				self.children.append(length_map[new_length])
			except(KeyError):
				new_node = TileNode(child, new_length)
				length_map[new_length] = new_node
				self.children.append(new_node)
			return True
		else:
			return False

	def num_leaves(self):
		if len(self.children) == 0:
			return 1
		else:
			try:
				return count_map[self.length]
			except(KeyError):
				count = sum(x.num_leaves() for x in self.children)
				count_map[self.length] = count
				return count

	def get_tile_str(self):
		if self.tile == None:
			return ''
		else:
			return str(self.tile)

	def get_all(self):
		if len(self.children) == 0:
			return [self.get_tile_str()]

		all_s = []
		for child in self.children:
			for combo in child.get_all():
				all_s.append(self.get_tile_str() + combo)
		return all_s 

	def __str__(self):
		s = '%s\t%d\n' % (self.tile, self.length)
		for x in self.children:
			for line in str(x).splitlines(True):
				try:
					s += '-' * self.tile.size + line
				except(AttributeError):
					s += line
		return s

tree = TileNode(None)
leaves_a = set([tree])
leaves_b = set([tree])

while not all(x.finished() for x in leaves_b):
	for leaf in leaves_a:
		if leaf.children == []:
			for tile in tile_choices:
				if not leaf.add_child(tile.get()):
					break

		leaves_b.remove(leaf)
		leaves_b |= set(leaf.children)

	leaves_a = copy.copy(leaves_b)

#print(tree)
print(tree.num_leaves())

