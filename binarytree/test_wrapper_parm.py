#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/1/3


# def test_fn(fn):
#     def wrapper(*args, **kwargs):
#         print(args)
#         print("------")
#         print(kwargs)
#         fn(*args, **kwargs)
#
#     return wrapper
#
#
# @test_fn
# def test(a, b, c, d):
#     print(a, b, c, d)
#
#
# test(1, 2, 3, 4)


class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class B(A):
    def do(self):
        print(self.a)


b = B(1, 2)
b.do()
