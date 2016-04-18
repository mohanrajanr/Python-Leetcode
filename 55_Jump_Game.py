# # # # -*- coding: utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)
        if length <= 1:
            return True
        # 用一个数组记录走到当前位置i时,可走的剩余最大步数
        jump = [0 for i in range(length)]
        jump[0] = nums[0]
        for i in range(1,length):
            jump[i] = max(jump[i-1],nums[i-1]) - 1
            if jump[i] < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,0,0]
    print s.canJump(nums)
    