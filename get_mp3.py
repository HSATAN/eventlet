# conding=utf8

import requests
url='http://static.missevan.com/MP3/201708/13/256b2f0bfdfda39188c487fb91807645103615.mp3'

name = url.split('/')[-1]
reponse=requests.get(url=url)
with open(name, 'wb') as f:
    f.write(reponse.content)

