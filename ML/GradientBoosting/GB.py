from sklearn.ensemble import GradientBoostingClassifier
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

model = GradientBoostingClassifier(learning_rate=0.01, n_estimators=1000, max_features='sqrt', subsample=0.80, random_state=10, max_depth= 100)

#-------------Training the model------------------#
print("#-------------Training the model------------------#")
model.fit(features_matrix, labels)


#-------------Predicting the output from Trained Model------------------#
print("#-------Predicting--------#")
predicted_labels = model.predict(test_feature_matrix)

print("#-------accuracy_score--------#")
print (accuracy_score(test_labels, predicted_labels))


