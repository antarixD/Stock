import random

class ScrappyKNN_randomClassifier():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predictions = []
        for row in x_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions

#---------------------------------------------------------------------------------#

from scipy.spatial import distance

def euclidean (a,b):
    return distance.euclidean(a,b)


class ScrappyKNN_Euclidean_Classifier():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predictions = []
        for row in x_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self,row):
        best_distance = euclidean(row, self.x_train[0])
        best_index = 0
        for i in range(1, len(self.x_train)):
            dist = euclidean(row, self.x_train[i])
            if dist < best_distance:
                best_distance = dist
                best_index = i
        return self.y_train[best_index]

from sklearn import datasets
iris = datasets.load_iris()

#iris has two parts data and target
input= iris.data
output = iris.target


#deviding the iris.data and iris.target into training and testing data set
from sklearn.model_selection import train_test_split
input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.3)

#importing the classifier from class ScrappyKNN
my_classifier = ScrappyKNN_Euclidean_Classifier()

#fitting and predicting the data
my_classifier.fit(input_train, output_train)
predictions = my_classifier.predict(input_test)

#checking the accurecy of testing inout and the testing output which is predicted by model

from sklearn.metrics import accuracy_score
print(accuracy_score(output_test,predictions))