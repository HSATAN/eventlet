#coding=utf8
from twisted.internet import reactor
from twisted.web import http
class MyRequestHandler(http.Request):

     resourse={
        '/': '<h1>Home</h1>fffffffffffffff page',
        '/about': '<h1>About</h1>All about me',
        }
     def process(self):
         self.setHeader("Content-Type","text/html")
         if self.resourse.has_key(self.path):
             self.write(self.resourse[self.path])
         else:
             self.setResponseCode(http.NOT_FOUND)
             self.write("<h1>not found</h1>")
         self.finish()

class MyHttp(http.HTTPChannel):
    requestFactory = MyRequestHandler
class MyHttpFactory(http.HTTPFactory):
    def buildProtocol(self, addr):
        return MyHttp()
reactor.listenTCP(9999,MyHttpFactory())
reactor.run()
