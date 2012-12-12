#!C:\Python33\python.exe

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p <= 1000, is the number of solutions maximised?

# Euclid's formula for Pythagorean triples:
# m^2 - n^2 : 2mn : m^2 + n^2
#
# Gets all primitive triples, must scale by k to get all triples

class Triangle(tuple):
	'''Triangle represented as tuple of sides (a,b,c).  Objects are considered identical
	regardless of the ordering of a and b.'''
	def __new__(cls, a, b, c):
		return tuple.__new__(cls, (a,b,c))

	def __eq__(self, other):
		return hash(self) == hash(other)

	def __hash__(self):
		a = self[0]
		b = self[1]
		c = self[2]
		return hash((a,b,c)) | hash((b,a,c))


def get_triangles(p_goal):
	goal_triangles = set()
	for n in range(1, p_goal):
		max_m = p_goal - n**2
		for m in range(n+1, max_m):
			max_k = int(p_goal / (m**2 + n**2))
			for k in range(1, max_k):

				a = k*(m**2 - n**2)
				b = 2*m*n*k
				c = k*(m**2 + n**2)

				p = a + b + c
				if (p > p_goal):
					# if we exceed the goal, consecutive values will only grow
					break
				elif (p == p_goal):
					goal_triangles.add(Triangle(a,b,c))
	return goal_triangles

for i in range(1,1000):
	s = get_triangles(i)
	if len(s):
		print(i, s)
