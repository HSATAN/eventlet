#coding=utf8
from twisted.internet.defer import Deferred
def mycallback(result):
    print result
def mycallback2(result):
    print result
d=Deferred()
d.addCallback(mycallback)
d.addCallback(mycallback2)
d.callback(("this defer callback","22"))
