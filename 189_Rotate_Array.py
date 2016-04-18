# # # # -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        result = []
        length = len(nums)
        k %= length
        # for i in range(length-k,length):
        #     result.append(nums[i])
        # for i in range(0,length-k):
        #     result.append(nums[i])
        result.extend(nums[length-k:])
        result.extend(nums[0:length-k])
        #print result
        nums = result
        for i in range(len(result)):
            nums[i] = result[i]
        print nums
        return

if __name__ == '__main__':
    s = Solution()
    nums = [1,2]
    k = 1
    s.rotate(nums,k)