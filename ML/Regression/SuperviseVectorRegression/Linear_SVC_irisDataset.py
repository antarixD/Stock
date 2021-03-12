import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC as SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris["data"][:, (2, 3)] # petal length, petal width

y = (iris["target"] == 2).astype(np.float64) # Iris-Virginica
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
# svm_clf = Pipeline((
# ("scaler", StandardScaler()),
# ("linear_svc", LinearSVC(C=1, loss="hinge")),
# ))  #96.66

svm_clf = SVC(C=1, loss="hinge")


svm_clf.fit(x_train, y_train)


predicted_labels = svm_clf.predict(x_test)
# Testing Model: Score returns the coefficient of determination R^2 of the prediction.
# The best possible score is 1.0
svm_confidence = svm_clf.score(x_test, y_test)
print("svm confidence: ", svm_confidence)


comparison = y_test == predicted_labels
equal_arrays = comparison.all()
print(comparison)
print(equal_arrays)
print (accuracy_score(y_test, predicted_labels))

# svm_clf.fit(X_scaled, y)
# Then, as usual, you can use the model to make predictions:
# >>> svm_clf.predic