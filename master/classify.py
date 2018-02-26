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
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline

from sklearn.model_selection import StratifiedKFold

import scipy
import pandas as pd
import numpy as np

# dftrain = pd.read_csv('distancetoverbtrain.csv')
# dftest = pd.read_csv('distancetoverbtest.csv')

dftest = pd.read_csv('distancetoverbtrain.csv')
dftrain = pd.read_csv('distancetoverbtest.csv')


# features = ['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PRE_DIST_STOPWORD', 'POST_DIST_STOPWORD', 'PrecedingTitle', 'Apostrophe', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION']

# features = ['PrecedingTitle', 'n-gram']

# features = ['PRE_DIST_VERB', 'POST_DIST_VERB', 'PRE_DIST_STOPWORD', 'POST_DIST_STOPWORD', 'PrecedingTitle', 'Apostrophe', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION']

features = ['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PrecedingTitle', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION', 'NEGATIVE_FEATURE', 'POSITIVE_FEATURE', 'Surrounding_Caps', 'POST_IS_PREPOSITION']


data = dftrain[features].as_matrix()
target = dftrain['classtype'].as_matrix()

# data, target = shuffle_in_unison(data, target)

fpl = []
fnl = []

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.1)
model = DecisionTreeClassifier()

model.fit(data, target)
print(model)

expected = dftest['classtype'].as_matrix()

predicted = model.predict(dftest[features].as_matrix())

n = len(expected)

for i in range(n):
    if expected[i] == False and predicted[i] == True:
        fpl.append(dftest.iloc[i])
    elif expected[i] == True and predicted[i] == False:
        fnl.append(dftest.iloc[i])

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

df = pd.DataFrame(np.array(fpl))
df.to_csv("fpl2.csv")

df = pd.DataFrame(np.array(fnl))
df.to_csv("fnl2.csv")


newmodel = SelectFromModel(model)

clf = Pipeline([
  ('feature_selection', newmodel),
  ('classification', DecisionTreeClassifier())
  ])
clf.fit(data, target)

l = zip(features, model.feature_importances_)
l.sort(key = lambda x:x[1], reverse=True)
print l


expected = dftest['classtype'].as_matrix()

predicted = clf.predict(dftest[features].as_matrix())
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
