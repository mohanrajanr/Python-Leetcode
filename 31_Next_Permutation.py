class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Algorithm: from the last index (on the right hand side) to the left, when nums[index] > nums[index-1],
        # if index reaches to the left (0) but no swap is done yet, reorder all elements from smallest to biggest

        for index in xrange(len(nums)-1, 0, -1):  # Pay attention to the end point! it should be nums[1], or otherwise when
                                                # it reaches to nums[0] the if condition below will be nums[-1]
            if nums[index] > nums[index-1]:
                # Then nums[index:] is descending; thus we should swap the nums[index-1] with number that in nums[i:] who
                # is just bigger than nums[index-1]
                # Example: [3,'2',4,'3',2,1]  ->  [3,'3',4,'2',2,1]
                for search in xrange(len(nums)-1, index-1, -1):
                    if nums[search] > nums[index-1]:
                        nums[search], nums[index-1] = nums[index-1], nums[search]
                        break
                # Then we should reorder nums[i:]
                # [3,'3',4,'2',2,1] -> [3,3,1,2,2,4]
                start = index
                end = len(nums) - 1
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                print nums
                return

        start = 0
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        print nums
        return


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    nums = [3,2,1]
    nums = [3,3,2,2]
    nums = [3,2,3,2]
    nums = [1,3,2]
    nums = [3,2,4,3,2,1]
    s.nextPermutation(nums)