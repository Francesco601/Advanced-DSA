# A Treap (portmanteau of Tree and Heap) is
# a self-balancing binary search tree. The idea
#is to use randomization and the Binary Heap
# property to maintain balance with high
# probability. The expected time complexity of
# search, insert and delete is O(log n).
#
# Every node of a Treap maintains two values.
# 1) Key: follows standard BST ordering (left
# is smaller and right is greater)
# 2) Priority: randomly assigned value that
# follows the Max-Heap property (each node
# has a key that is less than or equal to
# the key of its parent. Rotations are used
# after insertion and deletion to ensure that
# the Treap maintains the Max heap property.


# randomized second attribute of Treap
import random

# Node class for representing a node in the Treap
class Node:
    def __init__(self, key=None):
        self.key = key
        self.priority = random.randint(1, 100)
        self.left = None
        self.right = None


# Function to rotate right at a given node
def rotate_right(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root


# Function to rotate left at a given node
def rotate_left(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root


# Function to search for a key in the Treap
def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)

    return search(root.right, key)


# Function to insert a key into the Treap
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)

        if root.left.priority > root.priority:
            root = rotate_right(root)
    else:
        root.right = insert(root.right, key)

        if root.right.priority > root.priority:
            root = rotate_left(root)

    return root


# Function to delete a key from the Treap
def delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        if root.left.priority < root.right.priority:
            root = rotate_left(root)
            root.left = delete(root.left, key)
        else:
            root = rotate_right(root)
            root.right = delete(root.right, key)

    return root


# Utility function to print the Treap in inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)


# Test the Treap implementation
if __name__ == '__main__':
    root = None

    root = insert(root, 20)
    root = insert(root, 10)
    root = insert(root, 30)
    root = insert(root, 5)
    root = insert(root, 15)
    root = insert(root, 25)
    root = insert(root, 35)

    print("Inorder traversal after insertions:")
    inorder(root)
    print("\n")

    root = delete(root, 10)
    root = delete(root, 30)

    print("Inorder traversal after deletions:")
    inorder(root)

