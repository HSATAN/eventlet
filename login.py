# coding=utf8

import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'Referer':'http://www.missevan.com/member/login',
    'Origin':'http://www.missevan.com',
    'Host':'www.missevan.com'
}

data = {
    'LoginForm[username]': '18813045328',
    'LoginForm[password]': 'raybo2017'
}

url = 'http://www.missevan.com/member/login?backurl=%2F'



session = requests.session()
response = session.post(url=url, data=data)

url = 'http://www.missevan.com/sound/player?id=523732'

session.get(url)

print response.text