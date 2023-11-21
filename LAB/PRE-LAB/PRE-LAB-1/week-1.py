import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 8, 18, 32, 50, 72])

# Reshape the data to a 2D array
x = x.reshape(-1, 1)

# Create polynomial features
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# Fit the polynomial regression model
model = LinearRegression()
model.fit(x_poly, y)

# Predict using the model
y_pred = model.predict(x_poly)

# Plot the original data and the polynomial regression line
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Polynomial Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression with Degree 2')
plt.legend()
plt.show()
