import numpy as np
import matplotlib.pyplot as plt


class KMeans:
    def __init__(self, k=2, max_iters=100):
        self.k = k
        self.max_iters = max_iters

    def fit(self, X):
        self.centroids = X[np.random.choice(range(len(X)), self.k, replace=False)]

        for _ in range(self.max_iters):
            clusters = [[] for _ in range(self.k)]

            for point in X:
                distances = [np.linalg.norm(point - centroid) for centroid in self.centroids]
                closest_centroid = np.argmin(distances)
                clusters[closest_centroid].append(point)

            prev_centroids = self.centroids.copy()

            for i in range(self.k):
                if clusters[i]:
                    self.centroids[i] = np.mean(clusters[i], axis=0)

            if np.all(prev_centroids == self.centroids):
                break

    def predict(self, X):
        return [np.argmin([np.linalg.norm(x - centroid) for centroid in self.centroids]) for x in X]


# Example usage
X = np.array([[1, 2], [2, 1], [2, 4], [3, 2], [7, 2], [6, 4], [7, 3], [8, 4], [9, 5]])

kmeans = KMeans(k=2, max_iters=100)
kmeans.fit(X)
labels = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], marker='X', color='red')
plt.show()

