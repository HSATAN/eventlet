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

    get_count = 0
    post_count = 0
    def __init__(self):

        Resource.__init__(self)
        self.putChild('node', child_child())

    def render_GET(self, request):

        time.sleep(0.1)
        self.get_count += 1
        print 'get      ', self.get_count
        print request.args
        # request.write("我是子路径         ---")
        return bytes({"woshihuangkaijie"})
    def render_POST(self,request):

        self.post_count += 1
        print 'post    ',self.post_count

        print request.args.get('username',0)[0]
        time.sleep(0.1)
        return bytes(b"你发的是post请求")


class child_child(Resource):

    isLeaf = True
    def render_GET(self, request):
        return bytes("黄开杰")

reactor.listenTCP(9999,Site(busypage()))
reactor.run()