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
        self.putChild('wetest-73de419b25189dfe28a9ab524f9d618b.txt',yanzheng())

    def _delayedRender(self, request):
        request.write("finally done , at %s"%time.asctime())
        request.finish()

    def render_GET(self, request):
        d = deferLater(reactor,5,lambda :request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET

class yanzheng(Resource):
    get_count = 0
    post_count = 0
    isLeaf = True
    def __init__(self):
        Resource.__init__(self)
    def render_GET(self, request):
        return bytes("wetest-73de419b25189dfe28a9ab524f9d618b")

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

        print request.args.get('username',0)
        return bytes(b"你发的是post请求")


class child_child(Resource):

    isLeaf = True
    def render_GET(self, request):
        return bytes("黄开杰")
if __name__ == '__main__':

    reactor.listenTCP(9999,Site(busypage()))
    reactor.run()