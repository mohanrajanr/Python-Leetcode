# # # # -*- coding: utf-8 -*-
class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print (s.permute(nums))