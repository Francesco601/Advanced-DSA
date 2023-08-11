# Python Program to implement # iterative segment tree.
# The iterative version of the segment tree basically uses the fact, that for an index i,
# left child = 2 * i and right child = 2 * i + 1 in the tree.
# The parent for an index i in the segment tree array can be found
# by parent = i / 2. Thus we can easily travel up and down through
# the levels of the tree one by one. At first we compute the maximum in the ranges
# while constructing the tree starting from the leaf nodes and climbing up through the
# levels one by one. We use the same concept while processing the queries for finding the maximum in a range.
#
# Since there are (log n) levels in the worst case, so querying takes log n time.
# For update of a particular index to a given value we start updating the segment tree
# starting from the leaf nodes and update all those nodes which are affected by the updating of the
# current node by gradually moving up through the levels at every iteration. Updating also takes
# log n time because there we have to update all the levels starting from the leaf node
# where we update the exact value at the exact index given by the user.

from sys import maxsize
INT_MIN = -maxsize

def construct_segment_tree(a: list, n: int):
	global segtree

	# assign values to leaves of the segment tree
	for i in range(n):
		segtree[n + i] = a[i]

	# assign values to internal nodes
	# to compute maximum in a given range */
	for i in range(n - 1, 0, -1):
		segtree[i] = max(segtree[2 * i], segtree[2 * i + 1])

def update(pos: int, value: int, n: int):
	global segtree

	# change the index to leaf node first
	pos += n

	# update the value at the leaf node
	# at the exact index
	segtree[pos] = value

	while pos > 1:

		# move up one level at a time in the tree
		pos //= 2

		# update the values in the nodes in
		# the next higher level
		segtree[pos] = max(segtree[2 * pos], segtree[2 * pos + 1])

def range_query(left: int, right: int, n: int) -> int:
	global segtree

	# Basically the left and right indices will move
	# towards right and left respectively and with
	# every each next higher level and compute the
	# maximum at each height.
	# change the index to leaf node first
	left += n
	right += n

	# initialize maximum to a very low value
	ma = INT_MIN
	while left < right:

		# if left index in odd
		if left & 1:
			ma = max(ma, segtree[left])

			# make left index even
			left += 1

		# if right index in odd
		if right & 1:

			# make right index even
			right -= 1

			ma = max(ma, segtree[right])

		# move to the next higher level
		left //= 2
		right //= 2
	return ma


# Driver Code
if __name__ == "__main__":
	a = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33]
	n = len(a)

	# Construct the segment tree by assigning
	# the values to the internal nodes
	segtree = [0] * (2 * n)
	construct_segment_tree(a, n)

	# compute maximum in the range left to right
	left = 1
	right = 5
	print("Maximum in range %d to %d is %d" %
		(left, right, range_query(left, right + 1, n)))

	# update the value of index 5 to 32
	index = 5
	value = 32

	# a[5] = 32;
	# Contents of array : {2, 6, 10, 4, 7, 32, 9, 11, 6, 33}
	update(index, value, n)

	# compute maximum in the range left to right
	left = 2
	right = 8
	print("Maximum in range %d to %d is %d" %
		(left, right, range_query(left, right + 1, n)))


