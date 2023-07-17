# Python implementation and illustration of Splay Tree Deletion
# Following are the different cases which arise when one
# must delete from a splay tree.
# 1) Root is NULL: We simply return the root
# 2) Else Splay the given key k. If k is present, then it
# becomes the new root. If not present, then the last accessed
# leaf node becomes the new root.
# 3) If new root's key is not the same as k, the return the
# root as k is not present.
# 4) Else the key k is present.
#  4a) Split the tree into two trees. Tree1= root's left subtree
# and Tree2 = root's right subtree and delete the root node.
#  4b) Let the roots of Tree1 and Tree2 be Root1 and Root2 respectively,
# 4c)If Root is NULL, return Root2.
# 4d) Else, splay the max node (node having the maximum value) of
# Tree1.
#  4e) After the splay procedure, make Root2 as the right child of
# Root1 and return Root1.

# Node class for splay tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Splay tree class
class SplayTree:
    def __init__(self):
        self.root = None

    # Function to search for a key in the splay tree and splay the accessed node to the root
    def search(self, key):
        self.root = self.splay(self.root, key)
        return self.root.key == key

    # Function to insert a key into the splay tree
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self.splay(self.root, key)

        if self.root.key == key:
            return

        new_node = Node(key)

        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    # Function to delete a key from the splay tree
    def delete(self, key):
        if self.root is None:
            return

        self.root = self.splay(self.root, key)

        if self.root.key != key:
            return

        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root.right
            self.root = self.root.left
            self.root = self.splay(self.root, key)
            self.root.right = temp

    # Function to perform splay operation on the given key and return the new root
    def splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root

            if key < root.left.key:
                root.left.left = self.splay(root.left.left, key)
                root = self.rotate_right(root)
            elif key > root.left.key:
                root.left.right = self.splay(root.left.right, key)

                if root.left.right is not None:
                    root.left = self.rotate_left(root.left)

            if root.left is not None:
                return self.rotate_right(root)
            else:
                return root

        else:
            if root.right is None:
                return root

            if key < root.right.key:
                root.right.left = self.splay(root.right.left, key)

                if root.right.left is not None:
                    root.right = self.rotate_right(root.right)
            elif key > root.right.key:
                root.right.right = self.splay(root.right.right, key)
                root = self.rotate_left(root)

            if root.right is not None:
                return self.rotate_left(root)
            else:
                return root

    # Function to perform right rotation on the given node and return the new node
    def rotate_right(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp

    # Function to perform left rotation on the given node and return the new node
    def rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp

    # Function to print the splay tree in inorder traversal
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

# Creating splay tree object
splay_tree = SplayTree()
# Inserting elements into splay tree
splay_tree.insert(50)
splay_tree.insert(30)
splay_tree.insert(70)
splay_tree.insert(20)
splay_tree.insert(40)
splay_tree.insert(80)

# Printing the splay tree before deletion
print("Splay Tree before deletion:")
splay_tree.inorder_traversal(splay_tree.root)
print()

# Deleting elements from splay tree
splay_tree.delete(30)
splay_tree.delete(80)

# Printing the splay tree after deletion
print("Splay Tree after deletion:")
splay_tree.inorder_traversal(splay_tree.root)



