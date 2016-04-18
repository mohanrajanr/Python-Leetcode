# -*- coding: utf-8 -*-
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        if target <= nums[lo]:
            return lo
        if target > nums[hi]:
            return hi+1

        while lo < hi:
            mid = (lo + hi) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # this means target should be inserted on the right side of mid
                if nums[mid+1] >= target:
                    return mid+1
                else:
                    lo = mid + 1
            elif nums[mid] > target:
                if nums[mid-1] < target:
                    return mid
                else:
                    hi = mid - 1
        return

if __name__ == '__main__':
    s = Solution()
    #nums =[4, 5, 6, 7, 0, 1, 2]
    nums = [1, 3, 5, 6]
    target = 0
    print s.searchInsert(nums,target)