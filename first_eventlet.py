#coding=utf8
import eventlet
import time


def fetch(sock, addr):
    print addr

pool = eventlet.GreenPool()

eventlet.serve(eventlet.listen(("127.0.0.1",9999)),fetch)
