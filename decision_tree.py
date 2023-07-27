#This program first defines the entropy() function to calculate the entropy of a given set of labels y.
# Then, the split() function is defined to split a dataset X and its corresponding labels y into two subsets
# based on a feature and threshold value.

# Next, the find_best_split() function is implemented to find the best feature and threshold value to
# split the dataset. It iterates through all features and thresholds, calculates the information gain, and
# selects the split with the highest gain.

# The majority_vote() function is defined to determine the majority label in a given set of labels.
# This will be used when creating leaf nodes.

# The DecisionTree class is the main class that implements the decision tree algorithm. It has methods for
# fitting the model (fit()) and making predictions (predict()). The _grow_tree() method recursively constructs
# the decision tree by finding the best split and creating decision nodes until a stopping condition is met.

# Finally, the program tests the decision tree algorithm using a toy dataset and prints the predicted labels and actual labels for comparison.



import numpy as np
from collections import Counter

def entropy(y):
    counter = Counter(y)
    probabilities = [count / len(y) for count in counter.values()]
    return -np.sum(probabilities * np.log2(probabilities))

def split(X, y, feature_idx, threshold):
    mask = X[:, feature_idx] <= threshold
    return X[mask], y[mask], X[~mask], y[~mask]

def find_best_split(X, y):
    best_gain = 0
    best_feature = None
    best_threshold = None

    for feature_idx in range(X.shape[1]):
        unique_values = np.unique(X[:, feature_idx])

        for threshold in unique_values:
            X_left, y_left, X_right, y_right = split(X, y, feature_idx, threshold)
            left_entropy = entropy(y_left)
            right_entropy = entropy(y_right)
            total_entropy = (len(y_left) / len(y)) * left_entropy + (len(y_right) / len(y)) * right_entropy
            information_gain = entropy(y) - total_entropy

            if information_gain > best_gain:
                best_gain = information_gain
                best_feature = feature_idx
                best_threshold = threshold

    return best_feature, best_threshold

def majority_vote(y):
    counter = Counter(y)
    majority = counter.most_common(1)[0][0]
    return majority

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        if (depth <= self.max_depth if self.max_depth else True) and n_samples >= self.min_samples_split and n_labels > 1:
            best_feature, best_threshold = find_best_split(X, y)

            if best_feature is not None:
                X_left, y_left, X_right, y_right = split(X, y, best_feature, best_threshold)
                left_branch = self._grow_tree(X_left, y_left, depth + 1)
                right_branch = self._grow_tree(X_right, y_right, depth + 1)
                return DecisionNode(best_feature, best_threshold, left_branch, right_branch)

        return Leaf(majority_vote(y))

    def predict(self, X):
        return [self._predict(x) for x in X]

    def _predict(self, x):
        node = self.tree
        while isinstance(node, DecisionNode):
            if x[node.feature] <= node.threshold:
                node = node.left
            else:
                node = node.right
        return node.prediction

class DecisionNode:
    def __init__(self, feature, threshold, left, right):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right

class Leaf:
    def __init__(self, prediction):
        self.prediction = prediction

# Test the decision tree algorithm
X = np.array([[2.771244718,1.784783929],
    [1.728571309,1.169761413],
    [3.678319846,2.81281357],
    [3.961043357,2.61995032],
    [2.999208922,2.209014212],
    [7.497545867,3.162953546],
    [9.00220326,3.339047188],
    [7.444542326,0.476683375],
    [10.12493903,3.234550982],
    [6.642287351,3.319983761]])

y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

tree = DecisionTree(min_samples_split=2, max_depth=3)
tree.fit(X, y)
predictions = tree.predict(X)

print("Predicted labels:", predictions)
print("Actual labels:   ", y)
