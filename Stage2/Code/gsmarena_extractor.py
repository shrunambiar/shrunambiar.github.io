from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd
import numpy as np
import glob,os

# urls = ['output_0_61.html', \
# 'output_1_61.html', \
# 'output_2_61.html', \
# ]
# with open ("output_0_61.html", "r") as myfile:
#     data=myfile.readlines()
file_list = glob.glob("./gsm/*.html")
print file_list
urls = [1]

result = [{} for _ in range(len(file_list))]
featureset = set()
ctr = 0
for file in file_list:
    f= open (file, "r")
    data=f.read()

    # response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
    soup = BeautifulSoup(data, "html5lib")
    l = soup.find_all("title")
    name = ""
    for n in l:
        name = n.text.encode('utf-8')[:-28]

    featureset.add("Name")

    l = soup.find_all("div",{"id":"specs-list"})

    for b in l:
        # <td class="ttl">
        c = b.find_all("td", {"class":"ttl"})
        m = []
        for e in c:
            m.append(e.text.encode('utf-8'))
            featureset.add(e.text.encode('utf-8'))

        n = []
        # <td class="nfo">
        c = b.find_all("td", {"class":"nfo"})
        for e in c:
            n.append(e.text.encode('utf-8'))

        m.append("Name")
        n.append(name)

        # print m
        # print n
        f = zip(m, n)
        for e in f:
            # print "E", e
            result[ctr][e[0]] = e[1]
        ctr += 1
        # for e in f:
        #     print e
# print featureset

for r in result:
    temp = set(r.keys())
    remaining = featureset - temp
    for t in remaining:
        r[t] = "NaN"

df = pd.DataFrame.from_dict(result)
df.to_csv("1.csv")
