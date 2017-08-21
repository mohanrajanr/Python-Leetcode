# # # # -*- coding: utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        :param nums:
        :return:
        """
        length = len(nums)
        if length <= 2:
            return
        start = 0
        end = start + 1
        while start < length - 1:
            end = start + 1
            if nums[end] == nums[start]:
                start += 1
            else:
                for i in range(end, length):
                    if nums[i] == nums[start]:
                        self.swap(nums, end, i)
                        start += 2
                        break
        print nums

    def swap(self,nums,start,i):
        nums[start], nums[i] = nums[i], nums[start]

if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 2, 2, 1, 1, 2, 0]
    s.sortColors(nums)
    print len(nums)
    """
    start = 0  #0
    end = start + 1 #1
    if nums[end] is diff than nums[start], starting from end, search till the end and find if anything is equal to
    nums[start]: if yes then swap, start = start + 2 , else then just move start = start + 1 ->
    meaning before start the color is already sorted

    if nums[end] is the same as nums[start], start = start + 1, end = start + 1
    """

