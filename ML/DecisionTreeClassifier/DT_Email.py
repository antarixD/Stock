#https://medium.com/machine-learning-101/chapter-3-decision-tree-classifier-coding-ae7df4284e99

import  ML.naiveBayes.naiveBayes_GaussianNB as NB
from sklearn import tree
from sklearn.metrics import accuracy_score


train_loc = '/home/antarix/Desktop/naive bayes/test-mails (copy)'
#train_loc = '/home/antarix/Desktop/naive bayes/test-mails'
test_loc = '/home/antarix/Desktop/naive bayes/train-mails'
#______________________________Main________________________________________#
out_dir = NB.make_Dictionary(train_loc)
print ("reading and processing emails from file.")
features_matrix, labels = NB.extract_features(train_loc)
test_feature_matrix, test_labels = NB.extract_features(test_loc)

model = tree.DecisionTreeClassifier(min_samples_split=10)

#40 86.18
print ("Training model.")
#train model
model.fit(features_matrix, labels)
predicted_labels = model.predict(test_feature_matrix)
print ("FINISHED classifying. accuracy score : ")
print (accuracy_score(test_labels, predicted_labels))