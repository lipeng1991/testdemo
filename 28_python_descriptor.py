# coding=utf-8
# create by oldman at 2018/6/17

class Des(object):
    def __init__(self,init_value):
        self.value = init_value

    def __get__(self, instance, owner):
        print('call__get', instance, owner)
        return self.value

    def __set__(self, instance, value):
        print('call __set__', instance, value)
        self.value = value

    def __delete__(self, instance):
        print('call __delete__', instance)

    # def __setattr__(self, key, value):
    #     print('call __setattr__',key,value)
    #     self.value=value


class Widget():
    t = Des(1)


def main():
    w = Widget()
    print(type(w.t))
    w.t=1
    print(222222)
    print(w.t, Widget.t)
    print(333333)
    del w.t

if __name__=='__main__':
    main()