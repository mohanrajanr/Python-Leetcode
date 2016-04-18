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
        return self.dfs(candidates, target, 0)

    # 定义一个新的函数,函数参数为当前访问的节点i (i是candidates的index), candidates和target
    def dfs(self, candidates, target, start):
        """
        :param candidates:
        :param target:
        :param i: index of candidates
        :return: result 用于存储结果, List[List[int]]
        """
        result = []

        for i in range(start, len(candidates)):
            x = candidates[i]
            if target < candidates[i]:
                break
            if target == candidates[i]:
                result.append([target])
                return result
            if target > candidates[i]:
                # 在找到一个target=candidate[num]后,当前的y和candidates[num]会组成一个result, 所以应把他们合并
                # 合并后的result会被返回到上一层的result中
                # y的结果是下一层搜索的所有结果集, 在List[List[int]]中的每一个List[int]
                # candidates[num]是一个int, [candidates[num]]的类型是List[int], 通过+号可以和下一层的结果集合并
                # 如果y for y in self.dfs(candidates, target-candidates[num], num) 没有返回结果,则result也不会更新
                result += [[candidates[i]] + y for y in self.dfs(candidates, target-candidates[i], i)]

        return result

if __name__ == '__main__':
    s = Solution()
    #candidates = [2,3,6,7]
    #target = 7
    candidates = [2,3]
    target = 5

    print s.combinationSum(candidates,target)