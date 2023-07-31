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
"""



class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, node, start, end, idx, val):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def delete(self, node, start, end, idx):
        if start == end:
            self.arr[idx] = 0
            self.tree[node] = 0
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.delete(2 * node + 1, start, mid, idx)
            else:
                self.delete(2 * node + 2, mid + 1, end, idx)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node + 1, start, mid, l, r)
        p2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return p1 + p2

#driver code

arr = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(arr)
segment_tree.build(0, 0, segment_tree.n - 1)
print(segment_tree.query(0, 0, segment_tree.n - 1, 2, 4))  # Output: 21
segment_tree.update(0, 0, segment_tree.n - 1, 3, 6)
print(segment_tree.query(0, 0, segment_tree.n - 1, 2, 4))  # Output: 27
segment_tree.delete(0, 0, segment_tree.n - 1, 1)
print(segment_tree.query(0, 0, segment_tree.n - 1, 2, 4))  # Output: 23
