def cleanName(s):
    if "(" in s:
        i = s.index("(")
        s = s[:i]
    # else:
    #     print s


    printable = set(string.printable)
    s = filter(lambda x: x in printable, s)
    # ''.join(filter(lambda x: x in string.printable, s)
    return s


import pandas as pd
import string

df = pd.read_csv("./Table1.csv")

df['Name'] = df['Name'].apply(cleanName)

df.to_csv("updatedTable1.csv")

df = pd.read_csv("./Table2.csv")

df['Name'] = df['Name'].apply(cleanName)

df.to_csv("updatedTable2.csv")
