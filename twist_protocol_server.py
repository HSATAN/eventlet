#coding=utf8
from twisted.internet import reactor, protocol

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print data
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def  buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(9999,EchoFactory())
reactor.run()