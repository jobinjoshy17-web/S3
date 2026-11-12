from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size= 0.25, random_state= 42
)
model = GaussianNB()
model.fit(x_train, y_train)
y_prediction = model.predict(x_test)
acc = metrics.accuracy_score(y_test, y_prediction)
report = metrics.classification_report(y_test, y_prediction, target_names= iris.target_names)

print("Accuracy : ", acc * 100, "%")
print(report)

# Algorithm of Gaussian Naive Bayes
# 1. Import the required libraries.
# 2. Load the dataset.
# 3. Separate input features (X) and output labels (Y).
# 4. Split the dataset into training and testing data.
# 5. Create a Gaussian Naive Bayes model.
# 6. Train the model using training data.
# 7. Calculate the probability of each class using Gaussian distribution.
# 8. Predict the class labels for testing data.
# 9. Compare predicted output with actual output.
# 10. Calculate and display the accuracy.
