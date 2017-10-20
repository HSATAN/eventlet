# coding=utf8

import requests

from datetime import date, timedelta, datetime
import calendar
import time
import traceback
import pymysql
import psycopg2
from db import BaseDB
import psycopg2.extras
format_str = '%Y-%m-%d %H:%M:%S'

format_str_style_2 = '%Y%m%d%H%M%S'

date_key = 'statistics_date'
url='https://debugapi.raybo.com:2443/v1.0/live/live_sum_all'
url = 'https://debugapi.raybo.com:2443/admin/live/live_room_statistics'
url = 'http://172.16.10.134:9090/admin/live/live_room_statistics'

response = requests.get(url, params={'desc': 1})
print response.text