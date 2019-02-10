# # # # -*- coding: utf-8 -*-
"""
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).

对撞型指针问题，思路与Two Sum类似 O(n2) => O(n)
两个指针分别从数组的头跟尾向中间移动，相比于两次for循环，避免了不必要的扫描
---------------------
作者：ncst
来源：CSDN
原文：https://blog.csdn.net/sinat_32547403/article/details/54999439
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

def closestTwoSum(nums, target):
    import sys
    # Write your code here
    nums.sort()
    i, j = 0, len(nums) - 1
    diff = sys.maxint
    while i < j:
        if nums[i] + nums[j] < target:
            diff = min(diff, target - nums[i] - nums[j])
            i += 1
        else:
            diff = min(diff, nums[i] + nums[j] - target)
            j -= 1

    return diff

if __name__ == '__main__':
    array = [-1, 2, 1, -4]
    target = 4
    print(closestTwoSum(array, target))
