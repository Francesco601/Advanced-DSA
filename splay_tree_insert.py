# Python implementation of Splay Tree
# insertion. A splay tree is a self-balancing
# data structure where the last accessed key is
# always at the  root. The insertion operation
# is similar to a Binary Search Tree insert with
# some additional steps to ensure that the newly
# inserted ket becomes the new root and the splay
# structure is maintained.
#
# The following are different cases of inserting
# a key k into a splay tree.
# 1) Root is NULL. Simply allocate a new node and
# return it is root.
# 2) Splay the given key k. If k is already present, then
#it becomes the new root. If not, then the last accessed
# node becomes the new root.
# Node class to represent each node in the splay tree
# 3) If a new root's key is the same as k, do nothing,
# 4) Else allocate memory for new node and compare root's
# key with k.
# 4a) If k is smaller than root's key, make root the right
#child of new node, copy left child of root as left child of
# new node and set left child of root to NULL.
# 4b) If k is greater than root's ket, make toor the left
# child of new node, copy right child of root as right child
# of new node and make set right child of root to NULL.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Splay tree class
class SplayTree:
    def __init__(self):
        self.root = None

    # Function to perform a zig rotation
    def zig(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    # Function to perform a zag rotation
    def zag(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    # Function to perform splay operation
    def splay(self, key):
        if self.root is None or self.root.key == key:
            return

        dummy = Node(None)
        left_tree = dummy
        right_tree = dummy
        curr = self.root

        while True:
            if key < curr.key:
                if curr.left is None:
                    break
                if key < curr.left.key:
                    curr = self.zig(curr)

                if curr.left is None:
                    break

                right_tree.left = curr
                right_tree = curr
                curr = curr.left
                right_tree.left = None
            elif key > curr.key:
                if curr.right is None:
                    break
                if key > curr.right.key:
                    curr = self.zag(curr)

                if curr.right is None:
                    break

                left_tree.right = curr
                left_tree = curr
                curr = curr.right
                left_tree.right = None
            else:
                break

        left_tree.right = curr.left
        right_tree.left = curr.right
        curr.left = dummy.right
        curr.right = dummy.left

        self.root = curr

    # Function to insert a new element in the splay tree
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.splay(key)
            if key < self.root.key:
                new_node = Node(key)
                new_node.left = self.root.left
                new_node.right = self.root
                self.root.left = None
                self.root = new_node
            elif key > self.root.key:
                new_node = Node(key)
                new_node.right = self.root.right
                new_node.left = self.root
                self.root.right = None
                self.root = new_node

    # Function to print the elements of the splay tree (in-order traversal)
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

# Test the program
splay_tree = SplayTree()
splay_tree.insert(5)
splay_tree.insert(10)
splay_tree.insert(1)
splay_tree.insert(7)

print("Elements of splay tree after insertion: ")
splay_tree.inorder(splay_tree.root)
