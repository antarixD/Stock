# For division
from __future__ import division
# For Data Processing
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
#%matplotlib inline
from tabulate import tabulate


# For reading stock data from yahoo
#from pandas_datareader import DataReader

# import pip
# pip.main(['install', 'pandas_datareader'])
from pandas_datareader import DataReader


# For time stamps
from datetime import datetime



# List of Tech_stocks for analytics
tech_list = ['AAPL','GOOGL','MSFT','AMZN']

# set up Start and End time for data grab
end = datetime.now()
start = datetime(end.year-1,end.month,end.day)

#For-loop for grabing google finance data and setting as a dataframe
# Set DataFrame as the Stock Ticker

for stock in tech_list:
    globals()[stock] = DataReader(stock,'yahoo',start,end)

print(AAPL)
print("_________GOOGL________")

print(tabulate(GOOGL, headers='keys',tablefmt='psql'))