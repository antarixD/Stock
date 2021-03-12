#https://towardsdatascience.com/linear-regression-python-implementation-ae0d95348ac4

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

advertising_data = pd.read_csv('/home/antarix/Desktop/naive bayes/Advertising.csv')
print(advertising_data.head())
#drop Unnamed column
advertising_data = advertising_data.drop(['Unnamed: 0'], axis = 1)
print(advertising_data.head())

#We use matplotlib , a popular Python plotting library to make a scatter plot.
# STEP 1: Define the plot size
plt.figure('Name of the Graph',figsize=(16,8))
#STEP 2: Define x and y axis data
plt.scatter(advertising_data['TV'],advertising_data['sales'],c = 'black')
#STEP 3: Give naes to X and Y axis

plt.xlabel("Money spent on TV ads ($)")
plt.ylabel("Sales ($)")
#plt.show()

#converting the df to array. there are two ways
# use np.array(advertising_data['TV'])
# or use reshape(-1,1)
X = advertising_data['TV'].values.reshape(-1,1)
y = advertising_data['sales'].values.reshape(-1,1)
print (X)
print("-------------------------------------------------------")
print (np.array(advertising_data['TV']))

model = LinearRegression()
model.fit(X, y)

print("The linear model is: Y = {:.5} + {:.5}X".format(model.intercept_[0], model.coef_[0][0]))