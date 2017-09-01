# coding=utf8

import requests


param = {'name':'huangkaijie',
         'age':20}

data = {'username':'edison',
        'password':'你才'}
url = 'http://localhost:9999/child'
#response = requests.get(url,params=param)
pre = requests.post(url=url,data=data)
#print response.text
print pre.content.decode(encoding='utf8')