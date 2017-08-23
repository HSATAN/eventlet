# coding=utf8
from datetime import datetime,timedelta

from collections import defaultdict
class hkj(object):

    def __init__(self):
        self._test="huangkaijie"

class child(hkj):

    def ppp(self):
        self.__dict__

ins = child()
ins.ppp()
print ins._test