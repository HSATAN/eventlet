# coding=utf8
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

class busypage(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("second", second())
    def render_GET(self, request):
        return "woshihuangkaijie"

class second(Resource):
    isLeaf = True
    def render_GET(self, request):
        return "second"

if __name__ == '__main__':

    reactor.listenTCP(9999,Site(busypage()))
    reactor.run()