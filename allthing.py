# coding=utf8
from datetime import datetime,timedelta
import requests
from collections import defaultdict
class hkj(object):

    def __init__(self):
        self._test="huangkaijie"

class child(hkj):

    def ppp(self):
        self.__dict__

import time

timestamp = time.time()
time_local = time.localtime(timestamp)
dt = time.strftime("%Y-%m-%d",time_local)
print dt
print time.time()
