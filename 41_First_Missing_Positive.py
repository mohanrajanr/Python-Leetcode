# # # # -*- coding: utf-8 -*-
# https://leetcodenotes.wordpress.com/2013/07/17/first-missing-positive/
# # 给一个无序int array，有正有负，找第一个missing正整数。比如[3,4,-1,1] return 2.要求O(n)时间，O(1)空间。
# 思路：
# 要求这么高，还不让用空间换时间，说明不是dp，所以基本只让过一两遍数组，一边过一遍直接in place的改动数组（不让生成新数组啊）
# 既然是大部分不missing，所以可以用index来直接和元素产生关系。
# 试图让A[i]这个值x的index是x – 1，即每个index身上的元素都是index本身+1。所以{1 2 3}就是理想中的新数组，{1 5 3}就说明缺2。
# 算法：
# 如果A[i]不在自己该在的地方，就想办法把他换到该在的地方。如果A[i]是<=0或者A[i]比数组长度还大，说明没有它该在的地方，那就skip他，弄下一个（不用担心当前位置被它占了，如果后面有想在这个位置的正整数，它会被换走的）
# A[i]和A[A[i] – 1]换，然后继续回到i，接着换，直到第一种情况满足。但是如果这俩数一样，换也没用，就别原地打转了。
# 最后过一遍shift过的array，第一个不在原位的就是。


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            return 1 if nums[0] != 1 else 2

        i = 1

        while i < len(nums):
            curr_num = nums[i]
            if curr_num > len(nums) or curr_num <= 0:
                i += 1
            else:
                if nums[i] != nums[curr_num - 1]:
                    nums[curr_num - 1], nums[i] = nums[i], nums[curr_num - 1]
                else:
                    i += 1
        #print nums

        for i in range(0,len(nums)):
            if nums[i] != i+1:
                return i+1

        return nums[i] + 1



if __name__ == '__main__':
    s = Solution()
    #nums = [-1,2,0,2,3,5,1,-1]
    #j = [None]*max(l)
    nums = [2,1]
    print s.firstMissingPositive(nums)

