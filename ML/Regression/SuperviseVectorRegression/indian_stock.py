from datetime import date
from nsepy import get_history
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
import tensorflow as tf

# Stock options (for index options, set index = True)
stock_fut = get_history(symbol="JPPOWER",
 start=date(2020, 4, 1),
 end=date(2020, 5, 27),
 futures=False)
stock_fut.head()

print(stock_fut.columns)


# ------------------------------the below section is for derivatives ------------------------------
# stock_fut = get_history(symbol="HDFC",
#  start=date(2019, 1, 15),
#  end=date(2019, 2, 1),
#  futures=True,
#  expiry_date=date(2019, 2, 28))
# stock_fut.head()
# print(stock_fut)


opendf= stock_fut[['High']]


#now lets try and predict the open price of stock for next 10 days

forecast_days = 3
#add another column (Prediction) that will have predicted value for opening price after 10 days
opendf['Prediction'] = opendf[['High']].shift(-forecast_days)

### Create the independent data set (X)  #######
# Convert the dataframe to a numpy array
#get independent and dependent values
Training_input = np.array(opendf.drop(['Prediction'],1))
Training_output = np.array(opendf['Prediction'])


#lets remove last 10 rows from both input and output
Training_input = Training_input[:-forecast_days]
# the below 'dataToSeePrediction' will be used to predict the output from trained model
dataToSeePrediction = Training_input[-forecast_days:]


# removing the last 10 days of the data from Training_output
Training_output = Training_output[:-forecast_days]

# Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(Training_input, Training_output, test_size=0.2)

# Create and train the Support Vector Machine (Regressor)
#svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1 )
#svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf = Pipeline((
("scaler", StandardScaler()),
("linear_svc", SVR(kernel='rbf', C=1e3, gamma = 0.1)),
))

svr_rbf.fit(x_train, y_train)

# Testing Model: Score returns the coefficient of determination R^2 of the prediction.
# The best possible score is 1.0
svm_confidence = svr_rbf.score(x_test, y_test)
print("svm confidence: ", svm_confidence)

print(svr_rbf.predict(dataToSeePrediction))





# import matplotlib.pyplot as plt
# stock_fut.Close.plot(figsize=(10, 5))
# # Define the label for the title of the figure
# plt.title("Close Price", fontsize=16)
# # Define the labels for x-axis and y-axis
# plt.ylabel('Price', fontsize=14)
# plt.xlabel('Date', fontsize=14)
# # Plot the grid lines
# plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# plt.show()