# # # # -*- coding: utf-8 -*-
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                end -= 1
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False

if __name__ == '__main__':
    # nums = [1,3,1,1,1]
    # target = 3
    nums = [2,2,2,0,2,2]
    target = 0
    s = Solution()
    print(s.search(nums, target))
