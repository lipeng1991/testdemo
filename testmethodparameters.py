# coding=utf-8

class TestDemo1(object):

    def testmethod(self,a=1,b=[]):
        b.append(a)
        print(b)

if __name__=="__main__":
    TestDemo1().testmethod(a=1)
    TestDemo1().testmethod(a=3)