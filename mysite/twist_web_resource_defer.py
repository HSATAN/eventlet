# coding=utf8
from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site,NOT_DONE_YET
import time


class busypage(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild('child',child())
        self.putChild('',NoResource())

    def _delayedRender(self, request):
        request.write("finally done , at %s"%time.asctime())
        request.finish()

    def render_GET(self, request):
        d = deferLater(reactor,5,lambda :request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET


class child(Resource):


    def __init__(self):
        Resource.__init__(self)
        self.putChild('node', child_child())

    def render_GET(self, request):

        # request.write("我是子路径         ---")
        return {"woshihuangkaijie"}


class child_child(Resource):

    isLeaf = True
    def render_GET(self, request):
        return bytes("黄开杰")

reactor.listenTCP(9999,Site(busypage()))
reactor.run()