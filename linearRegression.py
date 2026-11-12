# Algorithm: Linear Regression

# 1. Start.
# 2. Load the Diabetes dataset.
# 3. Separate input features (X) and output (Y).
# 4. Split the dataset into training and testing data.
# 5. Create a Linear Regression model.
# 6. Train the model using training data.
# 7. Predict output using testing data.
# 8. Calculate Mean Squared Error (MSE).
# 9. Calculate R2 score.
# 10. Display the results and plot the graph.
# 11. Stop.

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load diabetes dataset
diabetes = datasets.load_diabetes()

# Select BMI feature
X = diabetes.data[:, 2:3] # BMI only
y = diabetes.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict output
y_pred = model.predict(X_test)

# Display results
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Plot graph
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue")
plt.xlabel("BMI")
plt.ylabel("Diabetes Progression")
plt.title("Linear Regression")
plt.show()
