# Logistic Regression
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import scipy
import pandas as pd
# fit a logistic regression model to the data

df = pd.read_csv('distance to verb.csv')
data = df[ ['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PRE_DIST_STOPWORD', 'POST_DIST_STOPWORD', 'PrecedingTitle', 'Apostrophe'] ].as_matrix()


target = df['classtype'].as_matrix()




model = LogisticRegression()
model.fit(data, target)
print(model)
print zip(['n-gram', 'PRE_DIST_VERB', 'POST_DIST_VERB', 'PRE_DIST_STOPWORD', 'POST_DIST_STOPWORD', 'PrecedingTitle', 'Apostrophe'], model.coef_[0])

print scipy.stats.pearsonr(df['PrecedingTitle'], target)
print scipy.stats.pearsonr(df['POST_DIST_STOPWORD'], target)

# make predictions
expected = target
predicted = model.predict(data)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
