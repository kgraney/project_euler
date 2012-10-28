#!/bin/env python3
import numpy as np

def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n / arrays[0].size
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out



class DiceRoller(object):
	def __init__(self, num_dice, face_values):
		self.num_dice = num_dice
		self.face_values = np.array(face_values)

	def results(self):
		'''
		return all the possible roll outcomes for this DiceRoller, which is the
		cartesian product across the num_dice-dimensional vector space where
		each dimension has the domain of values found in face_values
		'''
		return cartesian(self.num_dice*[self.face_values])

	def pdf(self):
		'''
		return the probability density function as a set of f(x) values with x
		taking all integers 0 through the length of the returned array
		'''
		out = np.bincount(np.sum(self.results(), axis=1))
		return out / np.sum(out)


# Define Colin and Peter's dice
PETER = DiceRoller(9, range(1,5))
COLIN = DiceRoller(6, range(1,7))

# Compute PDFs for Colin and Peter
colin_data = COLIN.pdf()
peter_data = PETER.pdf()

# Subtract the two PDFs to compute diff.  Where diff > 0 Peter will have beaten
# Colin.
diff = peter_data - colin_data
p = np.sum(diff[diff > 0])
print('%0.7f' % p)