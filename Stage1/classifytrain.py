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
from sklearn.metrics import precision_score, recall_score

import scipy
import pandas as pd
import numpy as np

# dftrain = pd.read_csv('distancetoverbtrain.csv')
# dftest = pd.read_csv('distancetoverbtest.csv')

dftrain = pd.read_csv('classifier_input_train.csv')

features = ['n-gram', 'POST_DIST_VERB', 'PrecedingTitle', 'PRE_DIST_FROM_POSITION', 'NEGATIVE_FEATURE', 'POSITIVE_FEATURE']


dataAll = dftrain[features].as_matrix()
target = dftrain['classtype'].as_matrix()
data = np.delete(dataAll, 0, 1)
# data, target = shuffle_in_unison(data, target)

fpl = []
fnl = []
data, target = shuffle_in_unison(data, target)

nsplits = 10
skf = StratifiedKFold(n_splits=nsplits)
skf.get_n_splits(data, target)
print(skf)

prec = 0
recall = 0

precwl = 0
recallwl = 0

for train_index, test_index in skf.split(data, target):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = target[train_index], target[test_index]

    # model = SVC()

    model = DecisionTreeClassifier()
    #GaussianNB()#DecisionTreeClassifier()#SVC()
    #LogisticRegression()
    model.fit(X_train, y_train)
    print(model)

    expected = y_test
    predicted = model.predict(X_test)

    n = len(expected)

    # for i in range(n):
    #     if expected[i] == False and predicted[i] == True:
    #         fpl.append(X_test[i])
    #     elif expected[i] == True and predicted[i] == False:
    #         fnl.append(X_test[i])

    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

    prec += precision_score(expected, predicted)
    recall += recall_score(expected, predicted)

    # using whitelist
    whitelist = ['Tony Blair', 'Alan Milburn', 'Charles Kennedy', 'David Blunkett', 'George Bush', 'Gordon Brown',
    'Michael Howard']
    whitelist = ['Tony Blair','Gordon Brown'] # 66


    whitelist2 = [w + "'s" for w in whitelist]

    blacklist = ['BBC']

    for i in range(n):
        # print dataAll[i][0]
        if predicted[i] == False and (dataAll[i][0] in whitelist or dataAll[i][0] in whitelist2):
            predicted[i] = True
        elif predicted[i] == True and dataAll[i][0] in blacklist:
            predicted[i] = False

    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

    precwl += precision_score(expected, predicted)
    recallwl += recall_score(expected, predicted)

    for i in range(n):
        if expected[i] == False and predicted[i] == True:
            fpl.append(dataAll[i])
        elif expected[i] == True and predicted[i] == False:
            fnl.append(dataAll[i])




print "avg prec", prec / nsplits
print "avg recall", recall / nsplits

print "avg prec wl", precwl / nsplits
print "avg recall wl", recallwl / nsplits

df = pd.DataFrame(np.array(fpl))
df.to_csv("fpl2.csv")

df = pd.DataFrame(np.array(fnl))
df.to_csv("fnl2.csv")
