#coding=utf8
from twisted.internet import reactor,protocol
class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.writeSequence(["huagnkaijie","xionglingtu"])#发送list
        #self.transport.write("")#发送字符串

    def dataReceived(self, data):
        print "server said: ",data
        print self.transport.getPeer()
        print self.transport.getHost()
        #self.transport.write("我已经收到了你的数据")
        #不能在客户端和服务器端的dataReceived中同时发送数据，不然会造成死循环
class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()
    def clientConnectionFailed(self, connector, reason):
        print "connection failed !"

    def clientConnectionLost(self, connector, reason):
        print "connect lost ",reason
        reactor.stop()
reactor.connectTCP("localhost",9999,EchoFactory())
reactor.run()