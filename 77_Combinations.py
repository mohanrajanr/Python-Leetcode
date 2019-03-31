# # # # -*- coding: utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if n == 0:
            return [[]]
        self.dfs(n, k, 1, [], res)
        return res

    def dfs(self, n, k, start, path, res):
        if k == 0:
            res.append(path[:]) # This is because later on path.remove(i) will remove the i in res too.
            # res.append(path[:]) will append the entire complete data copy
            # res.append(path) will only append the path reference, if the data in path changes then res also changes
            return

        for i in range(start, n+1):
            path.append(i)
            self.dfs(n, k-1, i+1, path, res)
            path.remove(i)


if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 2
    # print nums[0:1]
    # print nums[1:2]
    # print nums[0:1]+nums[1:2]
    print(s.combine(n,k))

