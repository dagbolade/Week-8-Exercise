# -*- coding: utf-8 -*-
"""GridSearchCVSampleCode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xSdATtInynplgPJvTFx9IvYkOljJtAj0
"""

from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.55, random_state=42)
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc = svm.SVC()
grid = GridSearchCV(svc, parameters,cv=10, scoring='accuracy', return_train_score=False,verbose=1)
grid.fit(X_train, y_train)
print("Best parameters found: ", grid.best_params_)
accuracy = grid.best_score_ *100
print("Training accuracy for our training dataset with tuning is: {:.2f}%".format(accuracy))
pred = grid.predict(X_test)
print("Test accuracy using: {:.2f}% ".format(accuracy_score(pred, y_test)*100))