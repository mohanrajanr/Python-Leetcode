# # # # -*- coding: utf-8 -*-
class Solution:
    def subarraySum(self, nums, k):
        dic = {0:1}
        res = pre_sum = 0
        for num in nums:
            pre_sum += num
            res += dic.get(pre_sum - k, 0)
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
        return res

    # def subarraySum1(self, nums, k):
    #     res = 0
    #     for i in range(len(nums)):
    #         prefix = 0
    #         for j in range(i, len(nums)):
    #             prefix += nums[j]
    #             if prefix == k:
    #                 res += 1
    #     return res

if __name__ == '__main__':
    s = Solution()
    nums = []
