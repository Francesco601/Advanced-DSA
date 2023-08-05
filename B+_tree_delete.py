# Python implementation of B+ Tree
# with insertions and deletion of one node
# while maintaining the tree balanced.
# Deletion from a B+ tree consists of three
# main events: searching the node where the
# key to be deleted exists, deleting the key
# and balancing them tree if required. Underflow
# is a situation where the number of keys in a
# node is less than the number of keys it
# should hold.
# 1) A node can have a  maximum of M children
# (three is used in below code).
# 2) A node can contain a maximum of M-1 keys
# (2 in this example code)
# 3) A node should have a minimum of [M/2] children
# (in this case 2).
# 4) A node (except root) should contain a minimum
# of [M/2] -1 keys (i.e 1 in this case).
# For more details on deletion algorithm see
# Wikipedia article. 

class Node:

		# Creating structure of tree
	def __init__(self, leaf = False):
		self.keys = []
		self.values = []
		self.leaf = leaf
		self.next = None

# B + Tree


class BPlusTree:
	def __init__(self, degree):
		self.root = Node(leaf = True)
		self.degree = degree

	# Search for key which
	# has to be deleted
	def search(self, key):
		curr = self.root
		while not curr.leaf:
			i = 0
			while i < len(curr.keys):
				if key < curr.keys[i]:
					break
				i += 1
			curr = curr.values[i]
		i = 0
		while i < len(curr.keys):
			if curr.keys[i] == key:
				return True
			i += 1
		return False

	# Insert key value pairs
	def insert(self, key):
		curr = self.root
		if len(curr.keys) == 2 * self.degree:
			new_root = Node()
			self.root = new_root
			new_root.values.append(curr)
			self.split(new_root, 0, curr)
			self.insert_non_full(new_root, key)
		else:
			self.insert_non_full(curr, key)

	def insert_non_full(self, curr, key):
		i = 0
		while i < len(curr.keys):
			if key < curr.keys[i]:
				break
			i += 1
		if curr.leaf:
			curr.keys.insert(i, key)
		else:
			if len(curr.values[i].keys) == 2 * self.degree:
				self.split(curr, i, curr.values[i])
				if key > curr.keys[i]:
					i += 1
			self.insert_non_full(curr.values[i], key)

	def split(self, parent, i, node):
		new_node = Node(leaf = node.leaf)
		parent.values.insert(i + 1, new_node)
		parent.keys.insert(i, node.keys[self.degree-1])
		new_node.keys = node.keys[self.degree:]
		node.keys = node.keys[:self.degree-1]
		if not new_node.leaf:
			new_node.values = node.values[self.degree:]
			node.values = node.values[:self.degree]

	def steal_from_left(self, parent, i):
		node = parent.values[i]
		left_sibling = parent.values[i-1]
		node.keys.insert(0, parent.keys[i-1])
		parent.keys[i-1] = left_sibling.keys.pop(-1)
		if not node.leaf:
			node.values.insert(0, left_sibling.values.pop(-1))

	def steal_from_right(self, parent, i):
		node = parent.values[i]
		right_sibling = parent.values[i + 1]
		node.keys.append(parent.keys[i])
		parent.keys[i] = right_sibling.keys.pop(0)
		if not node.leaf:
			node.values.append(right_sibling.values.pop(0))

	# Del the given key
	def delete(self, key):
		curr = self.root
		found = False
		i = 0
		while i < len(curr.keys):
			if key == curr.keys[i]:
				found = True
				break
			elif key < curr.keys[i]:
				break
			i += 1
		if found:
			if curr.leaf:
				curr.keys.pop(i)
			else:
				pred = curr.values[i]
				if len(pred.keys) >= self.degree:
					pred_key = self.get_max_key(pred)
					curr.keys[i] = pred_key
					self.delete_from_leaf(pred_key, pred)
				else:
					succ = curr.values[i + 1]
					if len(succ.keys) >= self.degree:
						succ_key = self.get_min_key(succ)
						curr.keys[i] = succ_key
						self.delete_from_leaf(succ_key, succ)
					else:
						self.merge(curr, i, pred, succ)
						self.delete_from_leaf(key, pred)
			if curr == self.root and not curr.keys:
				self.root = curr.values[0]
		else:
			if curr.leaf:
				return False
			else:
				if len(curr.values[i].keys) < self.degree:
					if i != 0 and len(curr.values[i-1].keys) >= self.degree:
						self.steal_from_left(curr, i)
					elif i != len(curr.keys) and len(curr.values[i + 1].keys) >= self.degree:
						self.steal_from_right(curr, i)
					else:
						if i == len(curr.keys):
							i -= 1
						self.merge(curr, i, curr.values[i], curr.values[i + 1])
				self.delete(key)

	def delete_from_leaf(self, key, leaf):
		leaf.keys.remove(key)
		if leaf == self.root or len(leaf.keys) >= self.degree // 2:
			return
		parent = self.find_parent(leaf)
		i = parent.values.index(leaf)
		if i > 0 and len(parent.values[i-1].keys) > self.degree // 2:
			self.rotate_right(parent, i)
		elif i < len(parent.keys) and len(parent.values[i + 1].keys) > self.degree // 2:
			self.rotate_left(parent, i)
		else:
			if i == len(parent.keys):
				i -= 1
			self.merge(parent, i, parent.values[i], parent.values[i + 1])

	def get_min_key(self, node):
		while not node.leaf:
			node = node.values[0]
		return node.keys[0]

	def get_max_key(self, node):
		while not node.leaf:
			node = node.values[-1]
		return node.keys[-1]

		def get_min_key(self, node):
			while not node.leaf:
				node = node.values[0]
				return node.keys[0]

	def merge(self, parent, i, pred, succ):
		pred.keys += succ.keys
		pred.values += succ.values
		parent.values.pop(i + 1)
		parent.keys.pop(i)
		if parent == self.root and not parent.keys:
			self.root = pred

	def fix(self, parent, i):
		node = parent.values[i]
		if i > 0 and len(parent.values[i-1].keys) >= self.degree:
			self.rotate_right(parent, i)
		elif i < len(parent.keys) and len(parent.values[i + 1].keys) >= self.degree:
			self.rotate_left(parent, i)
		else:
			if i == len(parent.keys):
				i -= 1
			self.merge(parent, i, node, parent.values[i + 1])

	# Balance the tree after deletion
	def rotate_right(self, parent, i):
		node = parent.values[i]
		prev = parent.values[i-1]
		node.keys.insert(0, parent.keys[i-1])
		parent.keys[i-1] = prev.keys.pop(-1)
		if not node.leaf:
			node.values.insert(0, prev.values.pop(-1))

	def rotate_left(self, parent, i):
		node = parent.values[i]
		next = parent.values[i + 1]
		node.keys.append(parent.keys[i])
		parent.keys[i] = next.keys.pop(0)
		if not node.leaf:
			node.values.append(next.values.pop(0))

	# Function to print Tree
	def print_tree(self):
		curr_level = [self.root]
		while curr_level:
			next_level = []
			for node in curr_level:
				print(str(node.keys), end =' ')
				if not node.leaf:
					next_level += node.values
			print()
			curr_level = next_level


# create a B + tree with degree 3
tree = BPlusTree(3)

# insert some keys
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)

# print the tree
tree.print_tree() # [4] [2, 3] [6, 7, 8, 9] [1] [5]

# delete a key
tree.delete(3)

# print the tree
tree.print_tree() # [4] [2] [6, 7, 8, 9] [1] [5]
