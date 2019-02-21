# # # # -*- coding: utf-8 -*-
# """
# 做法是，我们对每个有“1"的位置进行dfs，把和它四联通的位置全部变成“0”，这样就能把一个点推广到一个岛。
#
# 所以，我们总的进行了dfs的次数，就是总过有多少个岛的数目。
#
# 注意理解dfs函数的意义：已知当前是1，把它周围相邻的所有1全部转成0.
# """
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dirs = [
            [0, 1], # right
            [1, 0], # down
            [0, -1], # left
            [-1, 0], # up
        ]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)


if __name__ == '__main__':
    s = Solution()
    grid = [['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']]
    s.numIslands(grid)