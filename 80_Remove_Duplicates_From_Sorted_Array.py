# # # # -*- coding: utf-8 -*-
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        tail = 2
        for i in range(0, len(nums)):
            while tail < len(nums) and nums[tail] == nums[i]:
                nums.pop(tail)
            tail += 1
            if tail >= len(nums):
                break
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1]
    s.removeDuplicates(nums)
