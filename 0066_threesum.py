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
                if i < thre < j:
                    res.append([i, j, thre])
    return res


"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


def threeSumClosest(nums, target):
    nums.sort()
    sum_value = float("inf")
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            cur = nums[i] + nums[l] + nums[r]
            if cur == target: return target
            if abs(cur - target) < abs(sum_value - target):
                sum_value = cur
            if cur < target:
                l += 1
            if cur > target:
                r -= 1
    return sum_value


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
"""


def removeDuplicates(nums) -> int:
    if len(nums) == 0: return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
