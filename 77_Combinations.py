# # # # -*- coding: utf-8 -*-
class Solution1(object):
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

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        if n == 0:
            return [[]]
        nums = [x+1 for x in range(n)]
        for i in range(n): # i = 0 means nums[0], which is 1
            current_list = []
            current_list.append(nums[i])
            for j in range(i+1,n):
                current_list.append(nums[j])
                if len(current_list) == k:
                    result.append(current_list)
                    break
        return result


if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 3
    nums = [x+1 for x in range(n)]
    print nums
    # print nums[0:1]
    # print nums[1:2]
    # print nums[0:1]+nums[1:2]
    print s.combine(n,k)

