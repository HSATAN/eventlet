#coding=utf8

from twisted.internet import reactor
import time
def printTime():
    print "Current time is %s"%time.strftime("%H:%M:%S")

def stopReator():
    print "stopping reator"
    reactor.stop()

print time.strftime("%H:%M:%S")
reactor.callLater(2,printTime)
reactor.callLater(0,stopReator)
reactor.run()