def checktag(w):
    # print w
    l = w.split(" ")
    fw = l[0]
    lw = l[-1]
    if w.count("<n>") > 1 or w.count("</n>") > 1:
        return False

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
# from bs4 import BeautifulSoup

# df = pd.read_csv('listcleanfiles.csv')
df = pd.read_csv('listmarkedupfiles.csv')

list_of_files = df.filename.unique()

df['classtype'] = pd.Series(np.array([False for i in range(len(df))])) # all false
for fn in list_of_files:
    temp = df[df['filename'] == fn]
    index_list = list(temp.index)
    print fn

    for i in index_list:
        w = df.iloc[i]['All-Words']
        if checktag(w):
            df.at[i, 'classtype'] = True
        df.at[i, 'All-Words'] = cleanword(w)


df.to_csv("updatedlist.csv", sep=',',index=False)
