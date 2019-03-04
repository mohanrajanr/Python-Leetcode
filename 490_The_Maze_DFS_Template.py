# # # # -*- coding: utf-8 -*-
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        def dfs(x, y, stopped):
            # 如果当前节点已经访问过 则不继续DFS
            if (x, y) in stopped:
                return False
            # 将当前节点置为访问过
            stopped.add((x, y))
            # 如果当前节点已经是目标, 则返回
            if [x, y] == destination:
                return True
            # 对周围所有的方向进行访问,寻找下一个下标
            for i, j in ((-1, 0) , (1, 0), (0, -1), (0, 1)):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                # 对下一个下标DFS
                if dfs(newX, newY, stopped):
                    return True
            # 如果没有结果, 则返回False
            return False
        return dfs(start[0], start[1], set())

if __name__ == '__main__':
    s = Solution()
    maze = [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
            ]
    start = [0,4]
    destination = [4,4]
    print(s.hasPath(maze, start, destination))