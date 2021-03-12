import pandas as pd
import io
import requests
from tabulate import tabulate
from datetime import date,timedelta


from nsepy import get_history
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

path = '/home/antarix/Desktop/naive bayes/Stocks/registered_companies/MCAP_31032020_0.xlsx'
comp_list = pd.read_excel(path)
# filtering out the null values for column: symbol
filtered_df = comp_list[comp_list['Symbol'].notnull()]

symb = filtered_df.Symbol
symb = symb.reset_index(drop=True)

print(symb)

#print (tabulate(filtered_df,  headers='keys', tablefmt='psql'))

today = date.today()
last_day = (today - timedelta(1))
last_thirty_day = today - timedelta(365)
print('last_day: ', last_day)
print('last_thirty_day: ', last_thirty_day)




stock_fut = get_history(symbol="TCS",
 start=last_thirty_day,
 end=last_day,
 futures=False)
stock_fut.head()

base_price = stock_fut.head(1).High

print(tabulate(stock_fut,headers = 'keys', tablefmt = 'psql'))



column_to_drop = ['Symbol', 'Series']
stock_fut = stock_fut.drop(column_to_drop, axis = 1)
opendf= stock_fut


#now lets try and predict the open price of stock for next 10 days

forecast_days = 1
#add another column (Prediction) that will have predicted value for opening price after 1 days
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
predicted_price = svr_rbf.predict(dataToSeePrediction)

print('predicted_price: ', predicted_price)
print('base_price', base_price)
percent_growth = ((predicted_price- base_price)/base_price)*100
print('percent_growth: ', percent_growth)
# for ind in symb.index:
#      print(symb[ind])
#      company_symbol = symb[ind]
#      stock_fut = get_history(symbol=company_symbol,
#                              start=last_thirty_day,
#                              end=last_day,
#                              futures=False)
#      stock_fut.head()
#
#      print("-------------------------------------------------------------")

