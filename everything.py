# coding=utf8

import requests


param = {'name':'huangkaijie',
         'age':20}

data = {
        'password':'你才'}
url = 'http://localhost:9999/wetest-73de419b25189dfe28a9ab524f9d618b.txt'
#url = 'http://47.93.5.189:9999/wetest-73de419b25189dfe28a9ab524f9d618b.txt'
#response = requests.get(url,params=param)
pre = requests.get(url=url)
#print response.text
print pre.content.decode(encoding='utf8')