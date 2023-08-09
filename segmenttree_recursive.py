""" Python implementation of Segment Tree data structure.
A segment tree is a tree data structure used for storing
information about intervals, or segments. It allows
querying which of the stored segments contains a given
point.It is, in principle, a static data structure that 
cannot be modified once it has been built.
A segment tree for a set I of n intervals uses O(n log n)
storage and can be built in O(n log n) time. Segment
trees support search for all the intervals that contain
a query point in time O(log n +k), with k being the
number of retreived intervals or segments.
Characteristics:
1) A segment tree is a binary tree  with a leaf node
for each elemement in the array.
2) Each internal node represents a segment of range
of elements in the array.
3) The root node represents the entire array.
4)Each node stores information about the range it
represents, such as the sum or mimimun of the
elements in the segment.

The most common type of segment tree is the sum segment
tree. It stores the sum of elements in each segment
of the array and is used in problems where efficient
answer queries are needed about the sum of elements.

The code below first builds the segment tree using
the array elements. Then, it updates a specific element
in both the array and the segment tree. Finally, it finds
the maximum in a given range of the updated array using
the segment tree. The segment tree is represented as a list,
where each node of the tree stores the maximum value of its
corresponding range. The buildsegmenttree function is called
to construct the segment tree, while the updateelement function
updates a specific element. The findmaximum function is used
to find the maximum in a given range.
"""


# Function to build the segment tree
def build_segment_tree(arr, tree, node, start, end):
    # Base case: leaf node
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        # Recursively build left and right subtree
        build_segment_tree(arr, tree, 2*node + 1, start, mid)
        build_segment_tree(arr, tree, 2*node + 2, mid + 1, end)
        # Update the parent node with maximum value
        tree[node] = max(tree[2*node + 1], tree[2*node + 2])

# Function to update a specific element in the array and segment tree
def update_element(arr, tree, node, start, end, index, value):
    # Base case: leaf node
    if start == end:
        arr[index] = value
        tree[node] = value
    else:
        mid = (start + end) // 2
        if start <= index <= mid:
            # Update the left subtree
            update_element(arr, tree, 2*node + 1, start, mid, index, value)
        else:
            # Update the right subtree
            update_element(arr, tree, 2*node + 2, mid + 1, end, index, value)
        # Update the parent node with maximum value
        tree[node] = max(tree[2*node + 1], tree[2*node + 2])

# Function to find the maximum in a given range
def find_maximum(tree, node, start, end, l, r):
    # Base case: no overlap
    if l > end or r < start:
        return float('-inf')
    # Base case: complete overlap
    if l <= start and r >= end:
        return tree[node]
    mid = (start + end) // 2
    # Recursively find maximum in left and right subtree
    left_max = find_maximum(tree, 2*node + 1, start, mid, l, r)
    right_max = find_maximum(tree, 2*node + 2, mid + 1, end, l, r)
    # Return the maximum of left and right subtree
    return max(left_max, right_max)

# Example usage
arr = [1, 3, 2, 4, 6, 8]
n = len(arr)

# Build the segment tree
tree = [0] * (4*n)
build_segment_tree(arr, tree, 0, 0, n - 1)

# Find maximum in range [0, 3] before update
print(find_maximum(tree, 0, 0, n - 1, 0, 3))  # Output: 4

# Update value at index 2 to 7
update_element(arr, tree, 0, 0, n - 1, 2, 7)

# Find maximum in range [0, 3] after update
print(find_maximum(tree, 0, 0, n - 1, 0, 3))  # Output: 7
