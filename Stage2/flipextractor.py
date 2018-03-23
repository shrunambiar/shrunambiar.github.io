from bs4 import BeautifulSoup
import glob,os
import pandas as pd

def extract_flip(html):
    soup = BeautifulSoup(open(html), "html5lib")
    a = soup.find_all("div", class_="vmXPri col col-3-12")
    b = soup.find_all("ul", class_="_3dG3ix col col-9-12")
    c = soup.find_all("div", class_="_1vC4OE _37U4_g")
    d = soup.find_all("h1",class_="_3eAQiD")
    headers = [u'Name',u'Price_INR']
    
    for x in a:
        headers.append(x.get_text())

    data = pd.DataFrame(columns = headers)
    values = []
    for x in d:
        values.append(x.get_text().encode('utf-8'))
    for x in c:
        values.append(x.get_text().encode('utf-8')[1:])
    for x in b:
        values.append(x.get_text().encode('utf-8'))

    data.loc[0] = values

    return data

def start_extract(ls):
    original_columns = [u'Name', u'Price_INR', u'In The Box', u'Model Number', u'Model Name', u'Color', u'Browse Type',
                        u'SIM Type', u'Hybrid Sim Slot', u'Touchscreen', u'OTG Compatible',
                        u'Display Size', u'Resolution', u'Operating System', u'Processor Core',
                        u'Primary Clock Speed', u'Internal Storage', u'RAM',
                        u'Memory Card Slot Type', u'Primary Camera', u'Network Type',
                        u'Supported Networks', u'Battery Capacity', u'Warranty Summary']

    df = pd.DataFrame(columns = original_columns)
    for i in ls:
        df= pd.concat([df, extract_flip(i)], ignore_index=True)
    column_list = df.columns
    new_columns = list(set(column_list)-set(original_columns))
    original_columns.extend(new_columns)
    dk = df[original_columns]
    dk.to_csv("Extracted.csv", columns = original_columns, index = False)
    
file_list = glob.glob("./flipkart/*.html")
#ls = ['flipkartpage.html','flipkartpage2.html','flipkartpage3.html','flipkartpage4.html','flipkartpage5.html']
start_extract(file_list)

        
        
