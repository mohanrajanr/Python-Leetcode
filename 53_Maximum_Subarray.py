# # # # -*- coding: utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # MaxSubArray must be at least the max number from nums
        if nums is None:
            return 0

        max_ending_here = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            # max_ending_here 代表到当前节点时 得到和的最大值
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            # print max_ending_here
            result = max(max_ending_here, result)
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print s.maxSubArray(nums)