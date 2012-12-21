#!/usr/bin/env python
import numpy

# read in the matrix file
node_value = numpy.loadtxt('matrix.txt',
		dtype=numpy.uint64, delimiter=',')


source = (0,0)
destination = tuple([d - 1 for d in node_value.shape])
uint64_max = numpy.iinfo(numpy.uint64).max


# array of distances to nodes, initialized to uint64_max
distance = numpy.zeros(node_value.shape, dtype=numpy.uint64)
distance += uint64_max

# array of bools indicating if node has been reached yet
in_q = numpy.ones(node_value.shape, dtype=numpy.bool)

# array of uint64_max values for use with numpy.where()
maxes = numpy.zeros(node_value.shape, dtype=numpy.uint64)
maxes += uint64_max


# simplified Dijkstra's algorithm
distance[source] = node_value[source]
while (in_q.any()):
	candidates = numpy.where(in_q, distance, maxes)
	u = numpy.unravel_index(candidates.argmin(), candidates.shape)
	in_q[u] = False

	for v in [(u[0], u[1]+1), (u[0]+1,u[1])]:
		if v[0] > 79 or v[1]> 79:
			continue

		alt = distance[u] + node_value[v]
		if alt < distance[v]:
			distance[v] = alt

print(distance[destination])