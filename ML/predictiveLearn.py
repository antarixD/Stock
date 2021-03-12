#https://medium.com/datadriveninvestor/a-simple-guide-to-creating-predictive-models-in-python-part-2a-aa86ece98f86

import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('/home/antarix/Desktop/DataFiles/input.csv' )

df.info()
print(df.head())
print('print Df: ', df)


feat = df.drop(columns='Exited', axis=0, index=None)
label = df["Exited"]

print ('EXisted column: ', label)


#deviding the dataset into train and test splits.
#X_train is the training input and
X_train, X_test, y_train, y_test = train_test_split(feat, label, test_size=0.3)

# print('X_train: ', X_train)
# print('X_test: ', X_test)
# print('y_train: ', y_train)
# print('y_test: ', y_test)


# scaling the large numeric value

from sklearn.preprocessing import StandardScaler

sc_x = StandardScaler()
X_train = sc_x.fit(X_train)
X_test =sc_x.fit(X_test)

print("fit_x_train: ", X_train)
print("fit x test: ", X_test)

#--------------------------------------ML Starts-----------------------------------------#
