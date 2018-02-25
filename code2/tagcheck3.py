def checktag(w):
    # print w
    l = w.split(" ")
    fw = l[0]
    lw = l[-1]
    if fw[0:3] == "<n>" and lw[-4:] == "</n>":
        return True
    else:
        return False


def cleanword(w):
    w = w.replace("</n>", "")
    w = w.replace("<n>", "")
    return w

import pandas as pd
import numpy as np
import sys
from bs4 import BeautifulSoup

# df = pd.read_csv('listcleanfiles.csv')
df = pd.read_csv('listmarkedupfiles.csv')

list_of_files = df.filename.unique()

df['classtype'] = pd.Series(np.array([False for i in range(len(df))])) # all false
for fn in list_of_files:
    for i in range(0, len(df)):
        w = df.iloc[i]['All-Words']
        if checktag(w):
            df.at[i, 'All-Words'] = w[3:-4]
            df.at[i, 'classtype'] = True
        else:
            df.at[i, 'All-Words'] = cleanword(w)


df.to_csv("updatedlist.csv", sep=',',index=False)
