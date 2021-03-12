## https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23

# CrossEntropyLoss = -{ y log(y_hat) + (1-y) log(1-y_hat) }

import numpy as np
predictions = np.array([[0.25,0.25,0.25,0.25],[0.01,0.01,0.01,0.96]])
targets = np.array([[0,0,0,1],[0,0,0,1]])




def cross_entropy(predictions, targets, epsilon=1e-10):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce_loss = -np.sum(np.sum(targets * np.log(predictions + 1e-5)))/N
    return ce_loss

cross_entropy_loss = cross_entropy(predictions, targets)
print ("Cross entropy loss is: " + str(cross_entropy_loss))