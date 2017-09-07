# conding=utf8

import requests
url='https://debugapi.raybo.com:2443/v1.0/live/live_sum_all'
url = 'https://debugapi.raybo.com:2443/v1.0/live/close'
url = 'http://172.16.10.134:9090/admin/live/live_room_statistics'


parameter = {
'uid':999,
'live_id': 1024,
'spec': ' uid DESC',
'start_time': '2017-09-05 16:46:06'

}

import json
reponse=requests.get(url=url, params=parameter)
print reponse.request.url
print reponse.text

