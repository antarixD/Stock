#https://towardsdatascience.com/how-to-perform-lasso-and-ridge-regression-in-python-3b3b75541ad8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#GridSearchCV allow us to automatically perform 5-fold cross-validation with a range of different
# regularization parameters in order to find the optimal value of alpha.
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# DataPath = '/home/antarix/Desktop/naive bayes/Advertising.csv'
DataPath = 'D:/naive bayes/Advertising.csv'

#read the data
AdvertisingData = pd.read_csv(DataPath)
#Remove column 'Unnamed: 0'

Columns_toRemove = ['Unnamed: 0']
AdvertisingData = AdvertisingData.drop(Columns_toRemove, axis =1 )
#print(AdvertisingData.head(10))

#define a function to plot the different medium of advertisement against sales
def scatter_plot (Advertising_medium, sales):
    #defining the plot size
    Name_ofMedium = Advertising_medium
    plt.figure(Name_ofMedium, figsize=(16,8))
    plt.scatter(AdvertisingData[Advertising_medium], AdvertisingData[sales], c= 'red')
    #labeling the X and Y axis
    plt.xlabel("Money spent on {} ads $ ".format(Name_ofMedium))
    plt.ylabel("Sales $")
    plt.show()

#calling the plots
scatter_plot('TV', 'sales')
scatter_plot('radio', 'sales')
scatter_plot('newspaper', 'sales')
#conclusion:
#-----------
#As you can see from plots, TV and radio ads seem to be good predictors for sales,
# while there seems to be no correlations between sales and newspaper ads.

TrainingInput = AdvertisingData.drop(['sales'], axis = 1)
#Training_Output = np.array(AdvertisingData['sales'])
TrainingOutput = AdvertisingData['sales'].values.reshape(-1,1)
model = Ridge()

parameters = {'alpha':[-15,-10,-9,-4,-3,-2,1,5,10,20]}
Ridge_regressor = GridSearchCV(model, parameters, scoring='neg_mean_squared_error', cv=5)

Ridge_regressor.fit(TrainingInput,TrainingOutput)

print(Ridge_regressor.best_params_)
print(Ridge_regressor.best_score_)