from sklearn import datasets
iris = datasets.load_iris()


#iris has two parts data and target
input= iris.data
output = iris.target


#deviding the iris.data and iris.target into training and testing data set
from sklearn.model_selection import train_test_split
input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.3)


#importing K means
from sklearn.neighbors import KNeighborsClassifier
my_classifier  = KNeighborsClassifier()

#fitting and predicting the data
my_classifier.fit(input_train, output_train)
predictions = my_classifier.predict(input_test)

#checking the accurecy of testing inout and the testing output which is predicted by model

from sklearn.metrics import accuracy_score
print(accuracy_score(output_test,predictions))

