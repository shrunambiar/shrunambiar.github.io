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

import scipy
import pandas as pd
# fit a logistic regression model to the data

df = pd.read_csv('distance to verb.csv')
# features = ['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PRE_DIST_STOPWORD', 'POST_DIST_STOPWORD', 'PrecedingTitle', 'Apostrophe', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION']

# features = ['PrecedingTitle', 'n-gram']

# features = ['PRE_DIST_VERB', 'POST_DIST_VERB', 'PRE_DIST_STOPWORD', 'POST_DIST_STOPWORD', 'PrecedingTitle', 'Apostrophe', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION']

features = ['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PrecedingTitle', 'Apostrophe', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION']

data = df[features].as_matrix()


target = df['classtype'].as_matrix()


X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.33)#, random_state=42)


model = DecisionTreeClassifier()
#GaussianNB()#DecisionTreeClassifier()#SVC()
#LogisticRegression()
model.fit(X_train, y_train)
print(model)
# print zip(features, model.coef_[0])
#
# print scipy.stats.pearsonr(df['PrecedingTitle'], target)
# print scipy.stats.pearsonr(df['POST_DIST_STOPWORD'], target)

# make predictions
expected = y_test
predicted = model.predict(X_test)

n = len(expected)

for i in range(n):
    if expected[i] == False and predicted[i] == True:
        print df.iloc[i]['All-Words']


# l = zip(features, model.feature_importances_)
# l.sort(key = lambda x:x[1], reverse = True)
# print l
#
# tree.export_graphviz(model, out_file='tree1.dot')
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
#
# newmodel = SelectFromModel(model)
#
# clf = Pipeline([
#   ('feature_selection', newmodel),
#   ('classification', DecisionTreeClassifier())
#   ])
# clf.fit(X_train, y_train)
#
#
# expected = y_test
# predicted = clf.predict(X_test)
# # summarize the fit of the model
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))

# tree.export_graphviz(clf, out_file='tree2.dot')
