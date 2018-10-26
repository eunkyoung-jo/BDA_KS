# coding: utf-8
#2018/10/28

import requests
url='https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
data = resp.json()
data[0]['title']
import pandas as pd
issues = pd.DataFrame(data)
issues
issues = pd.DataFrame(data, columns=['url', 'html_url', 'title', 'id', 'user'])
writer = pd.ExcelWriter('data/issues.xlsx')
issues.to_excel(writer, 'fromGithub')
writer.save()
