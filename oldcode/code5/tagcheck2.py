def checktag(w):
    l = w.split(" ")
    fw = l[0]
    lw = l[-1]
    if fw[0:3] == "<n>" and lw[-4:] == "</n>":
        return True
    else:
        return False

def get_positives_from_file(filename):
    f = open(filename, "r")

    data = BeautifulSoup(f.read(), "lxml")
    l =[]
    for a in data.find_all('n'):
        temp = a.string

        l.append(temp.encode('ascii','ignore'))

    f.close()
    return l




import pandas as pd
import numpy as np
import sys
from bs4 import BeautifulSoup

df = pd.read_csv('list.csv')

list_of_files = df.filename.unique()

# df['classtype'] = pd.Series(np.random.randn(len(df))) # random
df['classtype'] = pd.Series(np.array([False for i in range(len(df))])) # random
# print df
for fn in list_of_files:
    positives = get_positives_from_file("./markedupfiles/" + fn[-7:])
    # print positives, fn
    # allinstances = df.loc[df['filename'] == fn]['All-Words']
    # print allinstances
    for i in range(0, len(df)):
        # print i
        w = df.iloc[i]['All-Words']
        # print "w", w, unicode(w, "utf-8"), unicode(w, "utf-8") in positives, positives
        # if unicode(w, "utf-8") in positives:
        # print w, w in positives, positives
        if w in positives:
            df.at[i, 'classtype'] = True
            # df.iloc[i]['classtype'] = True
            # print df
        # break

    # break

# print df

df.to_csv("updatedlist.csv", sep=',',index=False)
