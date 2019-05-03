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
w = 9  # 背包承受的最大重量

"""
0-1
我们有一个背包，背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，并且不可分割。我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？
"""


def f(weight, n, w):
    """
    动态规划
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


print(f(weight, n, w))


def f2(weight, n, w):
    """
    动态规划降低空间复杂度
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


print(f2(weight, n, w))

"""
背包问题升级
0-1
我们有一个背包，背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，价值不等，并且不可分割。我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总价值最大？
"""

maxW = 0
weight = [2, 2, 4, 6, 3]  # 每个物品的重量
value = [3, 4, 8, 9, 6]
n = 5  # 物品个数
w = 9  # 背包承受的最大重量


def f_2(weight, n, w, value):
    """
    动态规划
    :param value: 每个物品的价值
    :param weight: 每个物品的重量
    :param n: 物品个数
    :param w: 背包承受的最大重量
    :return:
    """
    states = [[-1] * (w+1) for i in range(0, n)]
    states[0][0] = 0
    states[0][weight[0]] = value[0]
    for i in range(1, n):  # 动态规划，状态转移
        for j in range(0, w + 1):  # 不选择第i个物品加入背包
            if states[i - 1][j] >= 0:
                states[i][j] = states[i - 1][j]
        for j in range(0, w - weight[i] + 1):  # 选择第i个物品加入背包
            if states[i - 1][j] >= 0:
                v = states[i - 1][j] + value[i]
                if v > states[i][j + weight[i]]:  # 合并每一层(i,cw)重复的状态，值记录cv最大的那个状态
                    states[i][j + weight[i]] = v
    maxvalue = -1
    for i in range(w, -1, -1):
        if states[n - 1][i] > maxvalue:
            maxvalue = states[n - 1][i]
    return maxvalue


print(f_2(weight, n, w, value))
