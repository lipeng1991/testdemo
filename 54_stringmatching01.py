#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/12/25
"""
>>> t = "this is a big apple,this is a big apple,this is a big apple,this is a big apple."
>>> p = "apple"
>>> bf(t, p)
4
>>> t = "为什么叫向量空间模型呢？其实我们可以把每个词给看成一个维度，而词的频率看成其值（有向），即向量，这样每篇文章的词及其频率就构成了一个i维空间图，两个文档的相似度就是两个空间图的接近度。假设文章只有两维的话，那么空间图就可以画在一个平面直角坐标系当中，读者可以假想两篇只有两个词的文章画图进行理解。"
>>> p = "读者"
>>> bf(t, p)
1
"""
import time
"""
字符串匹配算法
"""

def bf(t, p):
    """
    BF算法
    :param t:主串
    :param p:模式串
    :return:
    """
    start = time.time()
    i = 0
    count = 0
    while i <= len(t) - len(p):
        j = 0
        while t[i] == p[j]:
            if j == len(p) - 1:
                count += 1
                break
            i += 1
            j += 1

        else:
            i += 1
    print(count)
    print(time.time() - start)
    return count
