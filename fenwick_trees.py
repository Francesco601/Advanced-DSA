class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def get_prefix_sum(self, i):
        prefix_sum = 0
        while i > 0:
            prefix_sum += self.tree[i]
            i -= i & -i
        return prefix_sum

    def range_query(self, i, j):
        return self.get_prefix_sum(j) - self.get_prefix_sum(i-1)


# Example usage
arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
n = len(arr)

# Create a FenwickTree instance
ft = FenwickTree(n)

# Build the Fenwick tree
for i in range(1, n+1):
    ft.update(i, arr[i-1])

# Test prefix sum
print(ft.get_prefix_sum(5))  # Output: 15

# Test range query
print(ft.range_query(3, 8))  # Output: 13

# Update value at index 4
ft.update(4, 1)

# Test range query after updating
print(ft.range_query(3, 8))  # Output: 14

