# # # # # -*- coding: utf-8 -*-
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        matrix = [[0 for x in range(n+2)] for x in range(m+2)]
        # Add 0s to the surrounding of board
        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix[i][j] = board[i-1][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                current_sum = self.getSurroundingSum(matrix,i,j)
                if matrix[i][j] == 1:
                    if current_sum < 2 or current_sum > 3:
                        board[i-1][j-1] = 0
                    elif current_sum == 2 or current_sum == 3:
                        board[i-1][j-1] = 1
                else:
                    if current_sum == 3:
                        board[i-1][j-1] = 1
        #print board
        return

    def getSurroundingSum(self, matrix, i, j):
        return matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]


if __name__ == '__main__':
    s = Solution()
    board = [[1,0],[0,1],[1,1]]
    s.gameOfLife(board)