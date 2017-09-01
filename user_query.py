# conding=utf8

import requests
url='https://debugapi.raybo.com:2443/admin/chan_statistics/main'
#url = 'https://debugapi.raybo.com:2443/admin/account/userstate'

parameter={
'uid':992,
'session_data':'8d7671a5dd'

}
date_stamp = {
          "start_date":"20170504",
          "end_date": "20170510"
      }

reponse=requests.get(url=url, params=date_stamp)
print reponse.content

