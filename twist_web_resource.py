#coding=utf8
from twisted.internet import reactor
from twisted.web.server import resource
from twisted.web.server import Site
import time
class clockPage(resource.Resource):
    isLeaf=True
    def render_GET(self,request):
        return "the local time is %s"%time.ctime()
rs=clockPage()
reactor.listenTCP(9999,Site(rs))
reactor.run()