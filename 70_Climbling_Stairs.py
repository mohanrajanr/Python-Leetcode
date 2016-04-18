# # # # -*- coding: utf-8 -*-
# 简单秒杀DP题。加入ret[i]表示到达step i的方法数，由于step i只能从step i-1或step i-1分别爬1和2步到达，所以：
#
# 1. ret[i] = ret[i-1] + ret[i-2]
# 2. 起始条件：ret[1] = 1, ret[2] = 2
# 3. 事实上由于ret[i]只由前两个结果决定，并不需要储存整个队列。

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    # n = 5
    # [1,1,1,1,1]
    # [1,1,1,2]
    # [1,1,2,1]
    # [1,2,1,1]
    # [2,1,1,1]
    # [2,2,1]
    # [2,1,2]
    # [1,2,2]

    # n = 4
    # [1,1,1,1]
    # [1,1,2]
    # [1,2,1]
    # [2,1,1]
    # [2,2]

    # n = 3
    # [1,1,1]
    # [1,2]
    # [2,1]

    # n = 2
    # [1,1]
    # [2]

    # n = 1
    # [1]

    n = 5
    print s.climbStairs(n)