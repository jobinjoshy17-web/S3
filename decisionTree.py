from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size= 0.25, random_state= 42
)
model = DecisionTreeClassifier(criterion= 'entropy', max_depth= 4, min_samples_leaf= 2)
model.fit(x_train, y_train)
y_prediction = model.predict(x_test)
report = metrics.classification_report(y_test, y_prediction, target_names= iris.target_names)
print(report)

fig = plt.figure(figsize=(7, 2))
_ = tree.plot_tree(
    model, feature_names= iris.feature_names, class_names= iris.target_names, filled= True
)
plt.show()