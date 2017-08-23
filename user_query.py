# conding=utf8

import requests
url='https://debugapi.raybo.com:2443/v1.0/qixi_activity/userstate'

parameter={
'uid':992,
'session_data':'8d7671a5dd'

}
reponse=requests.get(url=url, params=parameter)
print reponse.content

