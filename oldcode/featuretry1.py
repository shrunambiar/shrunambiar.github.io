def checkCaps(instance):
    l = instance.split(" ")
    n = len(l)

    for ele in l:
        if ele[0].upper() != ele[0]:
            return False

    return True


def checkPrecedingPrefix(instance):
    l = instance.split(" ")
    # n = len(l)

    prefixes = ['Mr.', 'Mrs.', 'Dr.', 'Ms.', 'Sir.', 'Jr.', 'Sr.']

    if l[0] in prefixes or (l[0] + ".") in prefixes:
        return True

    return False

def checkSucceedingApostrophe(instance):
    l = instance.split(" ")
    # n = len(l)

    val = l[-1]

    if val[-1] == "\'" or val[-2:] == "\'s":
        return True

    return False


import pandas as pd
import numpy as np
import sys
from bs4 import BeautifulSoup
