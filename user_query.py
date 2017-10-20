# conding=utf8

import requests
import time
url = 'https://debugapi.raybo.com:2443/v1.0/live/live_sum_all'
url = 'https://debugapi.raybo.com:2443/admin/live/live_room_statistics'
url = 'http://172.16.10.134:9090/admin/live/live_room_statistics'
url = 'http://172.16.10.134:9090/v1.0/gift/list_new'

def access_log(func):
    def wrap(*args, **kwargs):
        print time.strftime("%Y-%m-%d", time.localtime(time.time()))
        return func(*args, **kwargs)
    return wrap

@access_log
def show(name):
    print name

parameter = {'in_live':1,
             'gift_type':1,
             'tuid':407,
             'app':1,
             'uid':407,
             'password':123456}

response = requests.get(url,params=parameter)
print response.text
