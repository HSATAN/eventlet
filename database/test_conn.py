# coding=utf8
from twisted.internet import reactor
from twisted.enterprise import adbapi
SQLDB_DSN_MASTER = {
    'w': 'dbname=peiwo user=huangkaijie password=raybo host=localhost',
    'r': 'dbname=peiwo user=huangkaijie password=raybo host=localhost'
}
dbpool=adbapi.ConnectionPool('psycopg2',SQLDB_DSN_MASTER['w'])

def getName(email):
    return dbpool.runQuery("SELECT * FROM test")

def printResult(result):
    print result
def finish():
    dbpool.close()
    reactor.stop()
d=getName("huangkaijie@qq.com")
d.addCallback(printResult)
reactor.callLater(1, finish)
reactor.run()
