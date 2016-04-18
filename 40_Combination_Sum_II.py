# # # # -*- coding: utf-8 -*-
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.dfs(sorted(candidates), target, 0)


    def dfs(self, candidates, target, start):
        result = []
        i = start
        while i < len(candidates):

            x = candidates[i]
            if x > target:
                break
            if x == target:
                result.append([target])
                return result
            if x < target:
                result += [ [x] + y for y in self.dfs(candidates, target-x, i+1) ]
                i += 1
                while i < len(candidates) and candidates[i] == x:
                    i += 1

        return result

if __name__ == '__main__':
    s = Solution()
    #candidates = [10,1,2,7,6,1,5]
    #target = 8
    #candidates = [1,1,1,6]
    #target = 8
    candidates = [1,1,6]
    target = 7
    print s.combinationSum2(candidates, target)
    #print [0 for x in range(4)]

    # 以[1,1,1,6]为例
    # 当搜索出y = [1,6]以后,此时的i为0,target为8,x为1, result为[1,1,6]
    # 说明当前的值(x)是1 , 若i+=1后的i对应的值也是x (candidates[i] == x), 则说明下一个值candidates[1]和当前值candidates[0]重复了
    # 如果马上进入到下次while循环 target没变,则当前的i会再次被引入到result中来
    # 注意result中已经包含从i往后的result 如果当前的i还在循环里则有重复