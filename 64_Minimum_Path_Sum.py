# # # # # -*- coding: utf-8 -*-
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # dp[i][j]是走到当前位置时的最小和
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

        #print dp
        return dp[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    grid = [[10]]
    print s.minPathSum(grid)