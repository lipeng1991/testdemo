#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/11
"""
使用栈实现括号的匹配判断
>>> judgment_brackets_matching(a)
    True
>>> judgment_brackets_matching(b)
    False
"""
open_brackets = '{[(<'
close_brackets = '}])>'
map_brackets = {'}': '{', ']': '[', ')': '(', '>': '<'}


def judgment_brackets_matching(rows):
    stack = []
    label = True
    for row in rows:
        if row in open_brackets:
            stack.append(row)
        elif row in close_brackets:
            if len(stack) < 1:
                label = False
                break
            elif map_brackets[row] == stack[-1]:
                stack.pop()
            else:
                label = False
                break
        else:
            continue
    if stack:
        label = False
    return label


# 测试用例
a = '<222qqq[{}({})111]>'
b = 'judkslajdklsa{}><'

assert judgment_brackets_matching(a) == True
assert judgment_brackets_matching(b) == False
