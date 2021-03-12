#https://medium.com/@randerson112358/predict-stock-prices-using-python-machine-learning-53aa024da20a

import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Get the stock data
quandl.ApiConfig.api_key = 'bfzvHe2KJCUhLpv2x-b2'
df = quandl.get("WIKI/AMZN")


# Take a look at the data
# print(df.head())


# Get the Adjusted Close Price
#df = df[['Adj. Close']]
df = df[['Open']]
# Take a look at the new data
# print(df.head())

# A variable for predicting 'n' days out into the future
forecast_out = 30 #'n=30' days
#Create another column (the target ) shifted 'n' units up
#df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)
df['Prediction'] = df[['Open']].shift(-forecast_out)
#print the new data set

# print(df.tail(100))


### Create the independent data set (X)  #######
# Convert the dataframe to a numpy array
X = np.array(df.drop(['Prediction'],1))
print(X)


#Remove the last '30' rows
X = X[:-forecast_out]
dataToSeePrediction = X[-30:]
print("dataToSeePrediction : ", dataToSeePrediction)


### Create the dependent data set (y)  #####
# Convert the dataframe to a numpy array
y = np.array(df['Prediction'])
# Get all of the y values except the last '30' rows
y = y[:-forecast_out]
print(y)


# Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the Support Vector Machine (Regressor)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)


# Testing Model: Score returns the coefficient of determination R^2 of the prediction.
# The best possible score is 1.0
svm_confidence = svr_rbf.score(x_test, y_test)
print()
print("svm confidence: ", svm_confidence)

print(svr_rbf.predict(dataToSeePrediction))


