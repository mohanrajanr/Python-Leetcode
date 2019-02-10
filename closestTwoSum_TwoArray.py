# # # # -*- coding: utf-8 -*-
"""
给两个数组。从两个数组中分别取一个数， 和要小于等于k。找到和最大的组合。
（其他描述：返回两个list中和最大但不超过一个值的下标－函数名optimalUtilization）
给2个sorted array，和一个整数capacity， 每个array各找出一个数，组成一个pair 。找出pair满足
以下条件：
1）sum of pair <= capacity
2) sum is maximum
后来真的遇到这道题的时候还是 先用O(N*N)的算法检查 了所有可能的组合，oj是可以过的。我觉
得这题的考点不在降低时间复杂度，而在不能 错过任何一个重复的组合.

"""

def optimalUtilization(array1, array2, capacity):
    max_sum = array1[0] + array2[0]
    if max_sum >= capacity:
        return [[0, 0]]
    result = []
    temp = []
    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            if array1[i] + array2[j] <= capacity:
                temp.append([i, j, array1[i] + array2[j]])
    temp = sorted(temp, key=lambda x: x[2], reverse=True)
    max_sum = temp[0][2]
    for t in temp:
        if t[2] == max_sum:
            result.append([t[0],t[1]])
    return result

if __name__ == '__main__':
    array1 = [0, 1, 2, 3, 4]
    array2 = [3, 4, 5]
    capacity = 8
    print(optimalUtilization(array1, array2, capacity))
