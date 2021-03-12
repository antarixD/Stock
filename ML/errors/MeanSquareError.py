#https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23
#https://www.statisticshowto.com/mean-squared-error/

import numpy as np
y_hat = np.array([0.000, 0.266, 0.333])
y_true = np.array([0.000, 0.254, 0.998])

def rmse(predictions, targets):
    #calculating the differences bw predicted and actual values
    differences = predictions - targets
    #squaring the differences (aka bais)
    differences_squared = differences ** 2
    #calculating the mean of all the bais
    mean_of_differences_squared = differences_squared.mean()
    #taking sqaure-root of mean_of_differences_squared
    rmse_val = np.sqrt(mean_of_differences_squared)
    return(rmse_val)

print("d is: " + str(["%.8f" % elem for elem in y_hat]))
print("p is: " + str(["%.8f" % elem for elem in y_true]))
rmse_val = rmse(y_hat, y_true)
print("rms error is: " + str(rmse_val))