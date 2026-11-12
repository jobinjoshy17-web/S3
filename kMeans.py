# Algorithm: K-Means Clustering

# 1. Start.
# 2. Load the dataset.
# 3. Select the number of clusters K.
# 4. Randomly initialize K centroids.
# 5. Calculate the distance between each data point
#    and all the centroids.
# 6. Assign each data point to its nearest centroid.
# 7. Calculate new centroids by finding the mean
#    of all data points in each cluster.
# 8. Repeat steps 5–7 until the centroids no longer
#    change or the maximum iterations are reached.
# 9. Display the clusters.
# 10. Stop.

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

iris = load_iris()
x = iris.data[:, :2] # all rows and the first 2 cols
y = iris.target

model = KMeans(n_clusters= 3, random_state= 21, n_init= 10)
model.fit(x)
labels = model.labels_

ari = adjusted_rand_score(y, labels)
nmi = normalized_mutual_info_score(y, labels)
print("adjusted_rand_score : ", ari)
print("normalized_mutual_info_score", nmi)

plt.subplot(1, 2, 1)
plt.scatter(x[:, 0], x[:, 1], c= iris.target)
plt.title("Actual")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.subplot(1, 2, 2)
plt.scatter(x[:, 0], x[:, 1], c=labels)
plt.title("Predicted")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()

# Algorithm of K-Means Clustering
# 1. Import the required libraries.
# 2. Load the dataset.
# 3. Select the input features.
# 4. Choose the number of clusters (K).
# 5. Initialize K random centroids.
# 6. Calculate the distance between data points and centroids.
# 7. Assign each data point to its nearest centroid.
# 8. Calculate new centroids for each cluster.
# 9. Repeat steps 6 to 8 until the centroids stop changing.
# 10. Display the final clusters.
