def shuffle_in_unison(a, b):
    assert len(a) == len(b)
    shuffled_a = np.empty(a.shape, dtype=a.dtype)
    shuffled_b = np.empty(b.shape, dtype=b.dtype)
    permutation = np.random.permutation(len(a))
    for old_index, new_index in enumerate(permutation):
        shuffled_a[new_index] = a[old_index]
        shuffled_b[new_index] = b[old_index]
    return shuffled_a, shuffled_b


# Logistic Regression
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline

from sklearn.model_selection import StratifiedKFold

import scipy
import pandas as pd
import numpy as np

# dftrain = pd.read_csv('distancetoverbtrain.csv')
# dftest = pd.read_csv('distancetoverbtest.csv')

dftrain = pd.read_csv('classifier_input_train.csv')

features = ['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PrecedingTitle', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION', 'NEGATIVE_FEATURE', 'POSITIVE_FEATURE', 'Surrounding_Caps','Apostrophe', 'POST_IS_PREPOSITION', 'RELATIONSHIP', 'POST_IS_SPEAK_VERB', 'PRE_IS_SPEAK_VERB']


data = dftrain[features].as_matrix()
target = dftrain['classtype'].as_matrix()

# data, target = shuffle_in_unison(data, target)

fpl = []
fnl = []
data, target = shuffle_in_unison(data, target)


skf = StratifiedKFold(n_splits=10)
skf.get_n_splits(data, target)
print(skf)

for train_index, test_index in skf.split(data, target):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = target[train_index], target[test_index]

    model = DecisionTreeClassifier()
    #GaussianNB()#DecisionTreeClassifier()#SVC()
    #LogisticRegression()
    model.fit(X_train, y_train)
    print(model)

    expected = y_test
    predicted = model.predict(X_test)

    n = len(expected)

    for i in range(n):
        if expected[i] == False and predicted[i] == True:
            fpl.append(X_test[i])
        elif expected[i] == True and predicted[i] == False:
            fnl.append(X_test[i])

    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
