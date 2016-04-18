# # # # -*- coding: utf-8 -*-
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ### Important!!!
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(0, len(nums)):
            rest_nums = nums[0:i] + nums[i+1:]
            #print rest_nums
            rest_nums_permute = self.permute(rest_nums)
            #print rest_nums_permute
            for x in rest_nums_permute:
                #print x
                x.append(nums[i])
                result.append(x)
            #for x in rest_nums_permute:
            #    print x
        #print result
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    # print nums[0:1]
    # print nums[1:2]
    # print nums[0:1]+nums[1:2]
    print s.permute(nums)