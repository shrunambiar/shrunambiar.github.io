# Logistic Regression
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier



import scipy
import pandas as pd
# fit a logistic regression model to the data

df = pd.read_csv('distance to verb.csv')
features = ['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PRE_DIST_STOPWORD', 'POST_DIST_STOPWORD', 'PrecedingTitle', 'Apostrophe', 'PRE_DIST_FROM_THE', 'PRE_DIST_FROM_POSITION']
data = df[features].as_matrix()


target = df['classtype'].as_matrix()




model = SVC()#LogisticRegression()
model.fit(data, target)
print(model)
# print zip(features, model.coef_[0])
#
# print scipy.stats.pearsonr(df['PrecedingTitle'], target)
# print scipy.stats.pearsonr(df['POST_DIST_STOPWORD'], target)

# make predictions
expected = target
predicted = model.predict(data)

n = len(expected)

for i in range(n):
    if expected[i] == True and predicted[i] == False:
        print df.iloc[i]


# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
