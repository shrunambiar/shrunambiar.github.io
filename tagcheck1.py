def checktag(w):
    l = w.split(" ")
    fw = l[0]
    lw = l[-1]
    if fw[0:3] == "<n>" and lw[-4:] == "</n>":
        return True
    else:
        return False


import pandas as pd
import numpy as np
import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]


f = open(filename, "r")

data = BeautifulSoup(f.read(), "lxml")

for a in data.find_all('n'):
    print a.string
