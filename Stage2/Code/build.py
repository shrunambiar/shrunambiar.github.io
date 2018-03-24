import csv

import sys
import numpy as np

f2 = open("map.csv", "rb")
r2 = csv.reader(f2)
d1 = {}
d2 = {}
d3 = {}
for r in r2:
    t1 = r[0].strip()
    t2 = r[1].strip()
    # print t1
    if t2 == 'None':
        # key in 1
        d1[t1] = t2
    elif t1 == 'None':
        # key in 2
        d2[t2] = t1
    else:
        # neither none
        # choose 1st as key
        d3[t1] = t2
f2.close()

for d in [d1, d2, d3]:
    print len(d.keys())
# final header
# d1(1, nan), d3(both), d2(nan, 2),

f = open("gsm.csv", 'rb')
reader = csv.reader(f)
headers = reader.next()
headers = [h.strip() for h in headers]
headers.extend(d2.keys())

f3 = open("f1.csv", "w")
w2 = csv.writer(f3)
w2.writerow(headers)
n = len(d2.keys())
for r in reader:
    temp = r[:]
    temp.extend([np.nan for _ in range(n)])
    w2.writerow(temp)

f3.close()
f.close()


f = open("flipkart.csv", 'rb')
reader = csv.reader(f)
headers = reader.next()
headers = [h.strip() for h in headers]
temp = d1.keys()
temp.extend(headers)

f3 = open("f2.csv", "w")
w2 = csv.writer(f3)
w2.writerow(temp)
n = len(d1.keys())
for r in reader:
    temp = [np.nan for _ in range(n)]
    temp.extend(r[:])
    w2.writerow(temp)

f3.close()

import pandas as pd

df1 = pd.read_csv("f1.csv")
l = list(df1)
temp = len(l)
l.sort()
# print l
l = d1.keys()
l.extend(d2.keys())
l.extend(d3.keys())
print len(l)

# print "d2", d2.keys()
# print "d3", d3.keys()
l.sort()
# print l
# temp = list(df1)
# temp.sort()
# print temp
df1 = df1[l]
df1.to_csv("f1.csv")

df2 = pd.read_csv("f2.csv")
l = list(df2)
l.sort()
# print l
l = d1.keys()
l.extend(d2.keys())
l.extend(d3.values())
l.sort()
print len(l)
df2 = df2[l]
df2.to_csv("f2.csv")

# print temp, len(l)
