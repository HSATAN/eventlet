# conding=utf8

import requests
url='https://debugapi.raybo.com:2443/admin/userinfo/user_query'

parameter={
  "host": "https://debugapi.raybo.com:2443",
  "env": {
    "app": 1,
    "version": 9999
  },
  "user": {
    "uid": 992,
    "password": "222222"
  },
  "tests": [
    {
      "api": "/admin/userinfo/user_query",
      "method": "GET",
      "params": {
        "uids": "992"
      },
      "except": {
        "type": "object",
        "properties": {
          "code": {
            "type": "number",
            "maximum": 0
          },
          "data": {
            "type": "object"
          }
        },
        "required": [
          "code"
        ]
      }
    }
  ]
}

reponse=requests.get(url=url,params=parameter)
print reponse