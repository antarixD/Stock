import pandas as pd
from sklearn import preprocessing
import numpy as np

history_points  = 50

csv_path = '/home/antarix/Desktop/naive bayes/Stocks/Data/TCS (copy).csv'
data = pd.read_csv(csv_path)
#data = data.drop(['Date','Symbol', 'Series', 'Trades','Deliverable Volume','%Deliverble'], axis=1)
data = data.drop(['Date', 'Symbol', 'Series', 'Trades'], axis=1)
data = data.drop(0, axis=0)
print(data.columns)
print(data.head)

data = data.values
print(np.array(data[:, 2]))


# data_normaliser = preprocessing.MinMaxScaler()
# data_normalised = data_normaliser.fit_transform(data)
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
# print(np.array(data_normalised[:,1]))
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
# print(data_normalised)

# using the last {history_points} open close high low volume data points, predict the next open value
#removing the first 50 values
ohlcv_histories_normalised = np.array([data[i:i + history_points].copy() for i in range(len(data) - history_points)])
next_day_open_values_normalised = np.array([data[:, 3][i + history_points].copy() for i in range(len(data) - history_points)])
next_day_open_values_normalised = np.expand_dims(next_day_open_values_normalised, -1)





next_day_open_values = np.array([data[:, 0][i + history_points].copy() for i in range(len(data) - history_points)])
# print("---------------------------------------------------------------------------------------")
# print(next_day_open_values)
next_day_open_values = np.expand_dims(next_day_open_values, -1)
# print("---------------------------------------------------------------------------------------")
# print(next_day_open_values)

y_normaliser = preprocessing.MinMaxScaler()
y_normaliser.fit(next_day_open_values)