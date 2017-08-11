#coding=utf8
from twisted.internet import reactor
from twisted.web.resource import Resource,NoResource
from twisted.web.server import Site
from calendar import calendar


class yearpage(Resource):
    def __init__(self,year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self,request):
        return "%s" % (calendar(self.year),)
class calendarhome(Resource):
    def getChild(self, path, request):
        if path=='':
            return self
        if path.isdigit():
            print path
            return yearpage(int(path))
        else:
            print path
            return NoResource()
    def render_GET(self,request):
        return "<html><body>Welcome to the calendar server!</body></html>"
root=calendarhome()
reactor.listenTCP(9999,Site(root))
reactor.run()