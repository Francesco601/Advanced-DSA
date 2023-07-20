"""
Implementing logistic regression for classification problem
Logistic regression is a machine learning technique used
for classification or prediction in data sets which have
many features, but where most of them have little value
and should be ignored

For example, imagine that you have several algorithms for
analyzing your photos. Some are good at converting images to
text, others are good at detecting objects in photos but not
for recognizing peopleìs faces, and others still focus on
finding patterns in color schemes.Now say you have an image
with two people in it: one smiling and the other frowning-
which one is the happier of the two? You need more than just
judging by appearances. You want to learn what makes people
happy and sad, so instead of having various algorithms that
each specialize in identifying different emotions, you want
an algorithm that knows how to recognize both emotions
equally well. In such cases, using a maching learning
algorithm like logistic regression can help you acheive
your goal more effectively.
For more information, see <https://www.kdnuggets.com/2022/07/logistic-regression-work.html>.
Other Helpful resources:
Coursera ML course
https://medium.com/@martinpella/logistic-regression-from-scratch-in-python-124c5636b8ac
"""
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

# get_ipython().run_line_magic('matplotlib', 'inline')


# In[67]:

# sigmoid function or logistic function is used as a hypothesis function in
# classification problems


def sigmoid_function(z):
    return 1 / (1 + np.exp(-z))


def cost_function(h, y):
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()


def log_likelihood(x, y, weights):
    scores = np.dot(x, weights)
    return np.sum(y * scores - np.log(1 + np.exp(scores)))


# here alpha is the learning rate, X is the feature matrix,y is the target matrix
def logistic_reg(alpha, x, y, max_iterations=70000):
    theta = np.zeros(x.shape[1])

    for iterations in range(max_iterations):
        z = np.dot(x, theta)
        h = sigmoid_function(z)
        gradient = np.dot(x.T, h - y) / y.size
        theta = theta - alpha * gradient  # updating the weights
        z = np.dot(x, theta)
        h = sigmoid_function(z)
        j = cost_function(h, y)
        if iterations % 100 == 0:
            print(f"loss: {j} \t")  # printing the loss after every 100 iterations
    return theta


# In[68]:

if __name__ == "__main__":
    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = (iris.target != 0) * 1

    alpha = 0.1
    theta = logistic_reg(alpha, x, y, max_iterations=70000)
    print("theta: ", theta)  # printing the theta i.e our weights vector

    def predict_prob(x):
        return sigmoid_function(
            np.dot(x, theta)
        )  # predicting the value of probability from the logistic regression algorithm

    plt.figure(figsize=(10, 6))
    plt.scatter(x[y == 0][:, 0], x[y == 0][:, 1], color="b", label="0")
    plt.scatter(x[y == 1][:, 0], x[y == 1][:, 1], color="r", label="1")
    (x1_min, x1_max) = (x[:, 0].min(), x[:, 0].max())
    (x2_min, x2_max) = (x[:, 1].min(), x[:, 1].max())
    (xx1, xx2) = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    probs = predict_prob(grid).reshape(xx1.shape)
    plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")

    plt.legend()
    plt.show()
