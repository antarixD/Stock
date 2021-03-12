# https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23
# https://www.statisticshowto.com/absolute-error/

import numpy as np

y_hat = np.array([0.000, 0.266, 0.333])
y_true = np.array([0.000, 0.254, 0.998])

def MAE(predictions,target):
    difference = target - predictions
    absolute_difference = np.absolute(difference)
    absolute_difference_mean = absolute_difference.mean()
    return absolute_difference_mean


meanAbsoluteError = MAE(y_hat,y_true)
print('The data is: ', y_true)
print('MeanAbsoluteError are: ', meanAbsoluteError )
