# # # # -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for j in range(0, n/2):
            for i in range(j, n-1-j):
                #t1, t2, t3, t4 = matrix[j][i], matrix[i][n-j-1], matrix[n-j-1][n-1-j-i], matrix[n-1-j-i][j]
                t1, t2, t3, t4 = matrix[j][i], matrix[i][n-j-1], matrix[n-j-1][n-1-i], matrix[n-1-i][j]

                matrix[j][i] = t4
                matrix[i][n-j-1] = t1
                matrix[n-j-1][n-1-i] = t2
                matrix[n-1-i][j] = t3
        # for i in range(0,n-1):
        #     t1, t2, t3, t4 = matrix[0][i], matrix[i][n-1], matrix[n-1][n-1-i], matrix[n-1-i][0]
        #     matrix[0][i] = t4
        #     matrix[i][n-1] = t1
        #     matrix[n-1][n-1-i] = t2
        #     matrix[n-1-i][0] = t3
        # print matrix
        return

if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    s.rotate(matrix)