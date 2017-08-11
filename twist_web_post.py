#coding=utf8
from twisted.web.resource import Resource
from twisted.web.server import Site
import cgi
from twisted.internet import reactor
import time

class formpage(Resource):
    isLeaf = True
    def render_GET(self,request):
        time.sleep(10)
        return """
        <html>
 <body>
  <form method="POST">
   <input name="form-field" type="text" />
   <input type="submit" />
   </form>
   </body>
   </html>
        """
    def render_POST(self,request):
        return """
        <html>
 <body>You submitted: %s</body>
 </html>
""" % (cgi.escape(request.args["form-field"][0]),)

reactor.listenTCP(9999,Site(formpage()))
reactor.run()