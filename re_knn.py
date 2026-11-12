from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# from matplotlib import pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size= 0.25, random_state= 42
)
model = KNeighborsClassifier(n_neighbors= 3)
model.fit(x_train, y_train)
y_prediction = model.predict(x_test)

acc = metrics.accuracy_score(y_test, y_prediction)
report = metrics.classification_report(y_test, y_prediction, target_names= iris.target_names)
print(acc * 100, "%")
print(report)

sample = [[5.1, 3.2, 4.1, 2.8]]
pred = model.predict(sample)[0]
print("New sample belongs to : ", iris.target_names[pred])

plt.subplot(1, 2, 1)
plt.scatter(x_test[:,0], x_test[:,1], c=y_prediction) # x-axis and y-axis
plt.title("Prediction")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.subplot(1, 2, 2)
plt.scatter(x_test[:,0], x_test[:,1], c=y_test)
plt.title("Actual")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()