#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/3
"""
动态规划：
动态规划比较适合用来求解最优问题，比如求最大值、最小值等。
我们把问题分解为多个阶段，每个阶段对应一个决策。我们记录每一个阶段可达的状态集合(去掉重复的)，
然后通过当前阶段的状态集合，来推导下阶段的状态集合，动态的王倩推进。这也是动态规划这个名字的由来。
"""
maxW = 0
weight = [2, 2, 4, 6, 3]  # 每个物品的重量
n = 5  # 物品个数
w = 20  # 背包承受的最大重量


def f(weight, n, w):
    """

    :param weight: 每个物品的重量
    :param n: 物品个数
    :param w: 背包承受的最大重量
    :return:
    """
    states = [[0] * (w + 1) for i in range(n)]
    states[0][0] = True  # 第一行数据要特殊处理，可以利用哨兵优化
    states[0][weight[0]] = True
    for i in range(1, n):  # 动态规划状态转移
        for j in range(0, w + 1):  # 不把第i个物品放进背包
            if states[i - 1][j]:
                states[i][j] = states[i - 1][j]
        for j in range(0, w - weight[i] + 1):
            if states[i - 1][j]:
                states[i][j + weight[i]] = True
    for i in range(w, -1, -1):
        if states[n - 1][i]:
            return i
    return 0


print(f(weight, 5, 20))


def f2(weight, n, w):
    """
    :param weight: 每个物品的重量
    :param n: 物品个数
    :param w: 背包承受的最大重量
    :return:
    """
    states = [0] * (w + 1)
    states[0] = True
    states[weight[0]] = True
    for i in range(1, n):
        for j in range(w - weight[i], -1, -1):
            if states[j]:
                states[j + weight[i]] = True
    for i in range(w, -1, -1):
        if states[i]:
            return i
    return 0


print(f2(weight, 5, 20))
