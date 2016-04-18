class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        i = 1
        count = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                count += 1
            i += 1
        return count

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,2,3,3,3,3,3,4]
    print s.removeDuplicates(nums)