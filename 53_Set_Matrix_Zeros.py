# # # # -*- coding: utf-8 -*-
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0]) # column
        m = len(matrix) # row
        used_row = [0 for i in range(0, m)]
        used_column = [0 for i in range(0, n)]
        # print used_column
        # print used_row
        for i in range(0, m):
            if used_row[i] == 1:
                continue
            for j in range(0, n):
                # if used_column[j] == 1:
                #     continue
                if matrix[i][j] == 0:
                    used_row[i] = 1
                    used_column[j] = 1
                    # for x in range(0, m):
                    #     matrix[x][j] = 0
                    # for y in range(0, n):
                    #     matrix[i][y] = 0
        print used_row
        print used_column
        for i in range(0, m):
            if used_row[i] == 1:
                for j in range(0, n):
                    matrix[i][j] = 0
        for j in range(0, n):
            if used_column[j] == 1:
                for i in range(0, m):
                    matrix[i][j] = 0
        print matrix
        return


if __name__ == '__main__':
    s = Solution()
    #matrix = [[0, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16],[17,18,19,20]]
    #matrix = [[0,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    s.setZeroes(matrix)