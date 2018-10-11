#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/11


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

if __name__ == '__main__':
    print(judgment_brackets_matching(a))
    print(judgment_brackets_matching(b))
