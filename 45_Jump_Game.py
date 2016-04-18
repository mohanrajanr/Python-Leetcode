# # # # -*- coding: utf-8 -*-
# https://leetcode.com/discuss/45992/10-lines-c-16ms-python-bfs-solutions-with-explanations
# 思路: 用广度优先搜索.每次搜索都会有一个区间[start,end],以当前区间内最大的i+nums[i]为当前区间所能到达的最远的距离,
# 如果这个距离比nums最大的index还要小,则搜索继续,搜索次数加一,直到找到比最大的index大的i+nums[i]为止.å

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = len(nums) - 1
        start, end = 0, 0

        step = 0
        while end < last:
            step += 1
            maxend = end + 1
            for i in range(start, end+1):
                if nums[i] + i >= last:
                    return step
                maxend = max(maxend, i + nums[i])
            start = end + 1
            end = maxend

        return step

    def jump1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        p = len(nums) - 1
        while p > 0:
            for i in range(0,p+1):
                if nums[i] + i >= p:
                    step += 1
                    p = i
                    break

        return step

if __name__ == '__main__':
    s = Solution()
    nums = [5,9,3,2,1,0,2,3,3,1,0,0]
    #nums = [2,3,1,1,4]
    print s.jump(nums)