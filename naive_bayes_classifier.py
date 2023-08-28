## In this example, we use the Iris dataset from scikit-learn. We split the dataset into training and 
# testing sets using the train_test_split function. Then, we initialize the Naive Bayes classifier using 
# the GaussianNB class and train the model using the fit method.
## Once the model is trained, we make predictions on the test set using the predict method. Finally,
## we calculate the accuracy of the model by comparing the predicted labels with the true labels and printing the accuracy score.
##Note that this implementation uses the Gaussian Naive Bayes algorithm, suitable for continuous input features. For categorical features, you can use CategoricalNB class instead.


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the Naive Bayes classifier
classifier = GaussianNB()

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
