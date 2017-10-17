# encoding=utf-8
import time


class TestDemo1:
    def fibonacci(self):
        """
        斐波那契 初始子序列
        """

        a, b = 0, 1
        while b < 100:
            print(b)
            a, b = b, a + b

    def test_for(self, list_test):
        """
        测试切片操作的浅拷贝
        """
        for item in list_test[:]:  # 所有的切片操作都会返回一个浅拷贝的副本,如果这里不用切片操作的话会是一个死循环
            if len(item) > 6:
                list_test.insert(0, item)

    def test_for_index(self,list_test):
        """
        测试for循环的操作是按照index执行的
        """
        for item in list_test:
            if len(item)>6:
                list_test.insert(0,item)
                list_test[3]='qqq' #替换最后一个数据的值,将其值长度换成小于6 的

    def test_num_value(self, para):
        """
        test for method's parameters are shallow copy except for num,string,tuple,this parameter is number
        """
        para = para + 1
        return para

    def test_string_value(self, para):
        """
        test for method's parameters are shallow copy except for num,string,tuple,this parameter is string
        """
        para = para + "nbbb"
        print(para)

    def test_for_exception(self,para):
        """
        test for exception is interrupt or not
        """
        for item in para:
            try:
                print(3/item)
            except Exception as e:
                print(e)

    def test_for_timer(self):
        time1=time.time()
        for i in range(0,400):
            print(i)
        time2=time.time()
        print(float(time2-time1))


# str="aaa"
# TestDemo1().test_string_value(str)
# print(str)
# num =1.3
# TestDemo1().test_value(num)
# print(num)
if __name__ == "__main__":
    # list_para = ['cat', 'window', 'defenestrate']
    # TestDemo1().test_for(list_para)
    # print(list_para)
    # TestDemo1().test_for_index(list_test=list_para)
    # print(list_para)

    # list_para=[0,1,2,3,4]
    # TestDemo1().test_for_exception(list_para)
    # TestDemo1().test_for_timer()

    dict_aa=dict({'aa' : 1, 'bb' :2, 'cc':33})
    print(len(dict_aa))