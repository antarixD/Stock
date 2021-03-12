import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

m = 100
X = 6 * np.random.rand(m, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)
print(type(X))
print(type(y))
z = X+y
print(z)
plt.scatter(X, y, label= "stars", color= "green",
            marker= "*", s=30)
plt.plot(X, y)
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)
X[0]
#array([-0.75275929])
X_poly[0]
#array([-0.75275929, 0.56664654])
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)
lin_reg.intercept_, lin_reg.coef_
plt.plot(lin_reg.intercept_, lin_reg.coef_)
plt.show()
