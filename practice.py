# _*_ coding: utf-8 _*_

class DESC(object):


    def __init__(self,initval=0):
        self.value = initval
        pass
    def __set__(self, instance, value):
        self.value=value
    def __get__(self, instance, value):
        return self.value
class TEST(object):
    x=DESC()
    y=DESC(10)
    def test(self):
        print "test"

ins = TEST()
print ins.x
print ins.y
ins.test()

print ins.__class__().test()

