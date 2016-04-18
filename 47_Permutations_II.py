# # # # -*- coding: utf-8 -*-
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute(sorted(nums))

    def permute(self, nums):
        ### Important!!!
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]

        result = []
        i = 0
        while i < len(nums):
            rest_nums = nums[0:i] + nums[i+1:]
            #print rest_nums

            rest_nums_permute = self.permute(rest_nums)
            #print rest_nums_permute
            for x in rest_nums_permute:
                #print x
                x.append(nums[i])
                result.append(x)

            i += 1
            while i < len(nums) and nums[i-1] == nums[i]:
                i += 1
            #for x in rest_nums_permute:
            #    print x
        #print result
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [3,3,0,0,2,3,2]
    # print nums[0:1]
    # print nums[1:2]
    # print nums[0:1]+nums[1:2]
    print s.permuteUnique(nums)