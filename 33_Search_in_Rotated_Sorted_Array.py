# -*- coding: utf-8 -*-
# 此题最难的地方不在于算法,而是在于while循环中start 和end的边界条件 - 何时有等号,何时start增加,何时end减少
class Solution(object):
    #
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.searchZone(nums, target, 0, len(nums)-1)

    def searchZone(self, nums, target, start, end):
        """
        try:
            result = nums.index(target)
        except:
            return -1
        return result
        """

        # Example 1: [3, 4, 5, 1, 2]
        # Example 2: [1, 2, 3, 4, 5]
        # Example 3: [4, 5, 1, 2, 3]
        result = -1

        if start == end:
            return 0 if target == nums[start] else result

        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[end]: # on left side of mid (including mid) is increasing
                if nums[start] <= target <= nums[mid]: # target is on left side, ascending zone
                    end = mid
                    result = self.binary_search(nums, target, start, end)
                    return result
                else:
                    # Note even we search partial nums, we still put nums as a complete array input to search()
                    # We just need to update start; should not call the recursion function again!
                    start = mid + 1
                    #result = self.searchZone(nums, target, start, end)
            elif nums[start] <= nums[mid] <= nums[end]: # list is in order
                result = self.binary_search(nums, target, start, end)
                return result
            elif nums[mid] < nums[start]: # on right side of mid (including mid) is increasing
                if nums[end] >= target >= nums[mid]: # target is on right side, ascending zone
                    start = mid
                    result = self.binary_search(nums, target, start, end)
                    return result
                else:
                    end = mid - 1
                    #result = self.searchZone(nums, target, start, end)

        return result

    def binary_search(self, a, x, lo=0, hi=None):
        if hi is None:
            hi = len(a) - 1
        while lo <= hi:
            mid = (lo+hi)//2
            midval = a[mid]
            if midval < x:
                lo = mid+1
            elif midval > x:
                hi = mid-1
            else:
                return mid
        return -1


if __name__ == '__main__':
    s = Solution()
    #nums =[4, 5, 6, 7, 0, 1, 2]
    nums = [5, 6, 7, 1, 2, 3]
    #nums = [1,3]
    target = 2
    print s.search(nums,target)