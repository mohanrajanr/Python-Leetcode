class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return 0



        # See https://leetcode.com/discuss/82281/four-line-easy-to-understand-python-solution for details
        # Diff between pop, remove and del
        # http://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
        for index in xrange(len(nums)-1,-1,-1):
            if nums[index] == val:
                nums.pop(index)

        # index = 0
        # count = 0
        # while index < len(nums):
        #     if nums[index] == val:
        #         nums.pop(index)
        #         count += 1
        #     else:
        #         index += 1
        #
        # return count

        return len(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,2,4,]
    #nums = [1]
    val = 2
    print s.removeElement(nums, val)