# # # # -*- coding: utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        :param nums:
        :return:
        """
        left = 0
        right = len(nums) - 1
        # first pass, will make all items that are smaller than 1 to be on the left zone
        for i in range(0, len(nums)):
            if nums[i] < 1:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        for i in range(len(nums)-1,left-1,-1):
            if nums[i] > 1:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
        return nums

if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 2, 2, 1, 0]
    s.sortColors(nums)
    print (nums)

