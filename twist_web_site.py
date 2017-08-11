#coding=utf8
'''
这个模块主要是实现资源和路径的映射

'''
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
root=File("mysite")
root.putChild("doc",File("twist_firse.py"))
factory=Site(root)
reactor.listenTCP(9999,factory)
reactor.run()
