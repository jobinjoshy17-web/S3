from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

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