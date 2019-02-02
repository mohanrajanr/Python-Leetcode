# # # # -*- coding: utf-8 -*-
#
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, lst, res):
        if target < 0:
            return
        if target == 0:
            res.append(lst)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], i, lst+[candidates[i]], res)


if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    # candidates = [2,3]
    # target = 5

    print (s.combinationSum(candidates,target))