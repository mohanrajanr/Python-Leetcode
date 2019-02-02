# # # # -*- coding: utf-8 -*-

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        return self.helper(result, nums, [], 0)

    def helper(self, result, nums, temp_list, n):
        result.append(temp_list)
        for i in range(n, len(nums)):
            self.helper(result, nums, temp_list+[nums[i]], i+1)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2]))
