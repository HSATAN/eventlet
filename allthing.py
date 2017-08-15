# coding=utf8
def test(**kwargs):
    conditions = []
    print type(kwargs)
    print kwargs.iteritems()
    for field,value in kwargs.iteritems():
        print field,value
        conditions.append('%s=%%s'%field)
    print conditions

test(name='huangkaijie', age=10)
