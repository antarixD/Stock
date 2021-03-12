from math import log

def calculateEntropy(dataSet):
  number = len(dataSet)
  labelCounts = {}
  for featureVector in dataSet:
    currentLabel = featureVector[-1]
    if currentLabel not in labelCounts.keys():
      labelCounts[currentLabel] = 0
    labelCounts[currentLabel] +=1
  entropy = 0
  for i in labelCounts:
    probability = float(labelCounts[keys])/number
    entropy -=probability*log(probability,2)
  return entropy

#-----------------main----------------------
train_loc = '/home/antarix/Desktop/naive bayes/test-mails (copy)'
#train_loc = '/home/antarix/Desktop/naive bayes/test-mails'
test_loc = '/home/antarix/Desktop/naive bayes/train-mails'


out  = calculateEntropy(train_loc)
print(out)