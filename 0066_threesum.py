#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/30
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def threeSum(nums):
    dict_nums = {}
    res = []
    if len(nums) < 3:
        return []
    for num in nums:
        dict_nums[num] = dict_nums.get(num, 0) + 1
    if 0 in dict_nums and dict_nums[0] >= 3:
        res.append([0, 0, 0])
    nums_gt_zero = list(filter(lambda x: x <= 0, dict_nums))
    nums_lt_zero = list(filter(lambda x: x > 0, dict_nums))
    for i in nums_gt_zero:
        for j in nums_lt_zero:
            thre = -i - j
            if thre in dict_nums:
                if thre in (i, j) and dict_nums[thre] >= 2:
                    res.append([i, j, thre])
                if thre > i and thre < j:
                    res.append([i, j, thre])
    return res