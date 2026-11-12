from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size= 0.25, random_state= 42
)

model = KNeighborsClassifier(n_neighbors= 3)
model.fit(x_train, y_train)
y_prediction = model.predict(x_test)
print("Accuracy : ", metrics.accuracy_score(y_test, y_prediction) * 100, "%")

sample = [[5.1, 3.5, 1.4, 0.2]]
pred = model.predict(sample)[0]
print("New sample belongs to : ", iris.target_names[pred])

plt.subplot(1, 2, 1)
plt.scatter(x_test[:,0], x_test[:,1], c=y_prediction)
plt.title("Predicted classification")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.subplot(1, 2, 2)
plt.scatter(x_test[:,0], x_test[:,1], c=y_test)
plt.title("Actual classification")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.show()

# Algorithm of KNN
# 1. Import the required libraries.
# 2. Load the dataset.
# 3. Separate input features (X) and output labels (Y).
# 4. Split the dataset into training and testing data.
# 5. Choose the value of K.
# 6. Calculate the distance between test data and training data.
# 7. Find the K nearest neighbors.
# 8. Count the class labels of the K neighbors.
# 9. Assign the majority class as the predicted output.
# 10. Compare predicted output with actual output.
# 11. Calculate and display the accuracy.
