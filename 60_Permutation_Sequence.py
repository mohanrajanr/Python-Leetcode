# # # # -*- coding: utf-8 -*-
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = self.permutenums(n)
        return result[k-1]
        #return self.permutenums(n,k)

    def permutenums(self, n):
        nums = [i+1 for i in range(n)]
        return self.permute(nums)

    def permute(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        count = 1
        result = []
        for i in range(0,len(nums)):
            for item in self.permute(nums[0:i]+nums[i+1:]):
                result.append(str(nums[i])+item)

        return result

if __name__ == '__main__':
    s = Solution()
    n = 3
    # nums = [i+1 for i in range(n)]
    # print nums
    #s.permute(n)
    # l1 = [1,2]
    # l2 = [3,4]
    # print l1+l2
    k = 2
    #print s.permutenums(n)
    print s.getPermutation(n,k)