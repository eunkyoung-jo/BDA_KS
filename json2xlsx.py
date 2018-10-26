# coding: utf-8
#2018/10/28
# refer to p.186~188 in Python for Data analysis

import requests
import pandas as pd


url='https://api.github.com/repos/pandas-dev/pandas/issues'
def json2xlsx(url, sheetname='sheet1', filename='out.xlsx'):

    resp = requests.get(url)
    data = resp.json()
    data[0]['title']
    issues = pd.DataFrame(data)
    issues
    issues = pd.DataFrame(data, columns=['url', 'html_url', 'title', 'id', 'user'])
    writer = pd.ExcelWriter(filename)
    issues.to_excel(writer, sheetname)
    writer.save()

def xlsx2txt(xlsfn, outfn='out.txt'):
    data = pd.read_excel(xlsfn, index_col=None, headers=None)
    #data = pd.read_excel(xlsfn)
    print(data)
    data.to_csv(outfn, sep='\t')

if __name__ == "__main__":
    #json2xlsx(url)
    #xlsx2txt('out.xlsx')
    json2xlsx(url, 'fromGithub', 'data/issues.xlsx')
