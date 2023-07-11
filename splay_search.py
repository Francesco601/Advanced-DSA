# A Splay Tree is a self-balancing binary search
# tree with the additional property that recently
# accessed elements are likely to be accessed
# again. All normal operations on a binary
# search tree are combined with one basic operation
# called "splaying". Splaying the tree for a certain
# element rearranges the tree so that the element
# is placed at the root of tree. This is done by perfoming
# the basic binary tree search for the desired element,
#and then using tree rotations (like with AVL trees)
# in a specific fashion to get the element to the top
#
# Like self-balancing BSTs, a splay tree performs
# basic operations such as inserion,search and deletion
# on O(log n) amortized time.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return self._splay(node, key)

    def search(self, key):
        self.root = self._splay(self.root, key)
        if self.root and self.root.key == key:
            return True
        return False

    def _splay(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            if node.left is None:
                return node
            if key < node.left.key:
                node.left.left = self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.key:
                node.left.right = self._splay(node.left.right, key)
                if node.left.right is not None:
                    node.left = self._rotate_left(node.left)

            if node.left is not None:
                return self._rotate_right(node)
            else:
                return node

        else:
            if node.right is None:
                return node
            if key < node.right.key:
                node.right.left = self._splay(node.right.left, key)
                if node.right.left is not None:
                    node.right = self._rotate_right(node.right)
            elif key > node.right.key:
                node.right.right = self._splay(node.right.right, key)
                node = self._rotate_left(node)

            if node.right is not None:
                return self._rotate_left(node)
            else:
                return node

    def _rotate_right(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp

    def _rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp


# Example usage:
tree = SplayTree()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(3)

print(tree.search(20))  # Output: True
print(tree.search(15))  # Output: False
