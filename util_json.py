#2018/10/28
# coding: utf-8
import requests, json
import pandas as pd

def show_json_data(key='', url=None):
    if url is None:
        json_str='{"one" : "하나", "two" : "둘", "three" : "셋"}'
        json_data = json.loads(json_str)
        print(json_data)
        print(json_data.get(key, 'None'))
        return
    #if url is given
    wdata = requests.get(url)
    jdata = json.loads(wdata.text) # == wdata.json()
    for jele in jdata:
        print(jele.get('url', 'None'))
        print('[title]', jele.get('title', 'None'))

def json2xlsx(url, sheetname='sheet1', filename='out.xlsx'):
    resp = requests.get(url)
    data = resp.json()
    issues = pd.DataFrame(data)
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

    url='https://api.github.com/repos/pandas-dev/pandas/issues'
    show_json_data('three')
    show_json_data('five')
    show_json_data(url=url)
    json2xlsx(url, 'fromGithub', 'data/issues.xlsx')
    #json2xlsx(url)
    #xlsx2txt('out.xlsx')
