# # # # -*- coding: utf-8 -*-
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        # Get the first column values in matrix
        firstColValues = [matrix[i][0] for i in xrange(m)]
        # Search in first column
        flag, row_location = self.binarySearch(firstColValues, target, 0, m-1)
        # If target value is not in first column values, then we move onto row search
        if flag:
            return True
        else:
            searchRange = m-1 if row_location+1 > m else row_location+1
            for i in range(searchRange):
                flag, col_location = self.binarySearch(matrix[i], target, 0, n-1)
                if flag:
                    return True
        return False

    def binarySearch(self, array, target, start, end):
        """
        :type array: List
        :type target: int
        :type start: int
        :type end: int
        :rtype: bool
        """
        mid = (start + end)/2
        while start < end:
            mid = (start + end)/2
            if target == array[mid]:
                return True, mid
            elif target < array[mid]:
                end = mid
            elif target > array[mid]:
                start = mid + 1
        mid = (start + end)/2
        if array[mid] == target:
            return True, mid
        # Note it is possible the target is out of bound, thus we need to consider the boundry situation
        if array[mid] < target:
            return False, mid
        return False, mid-1

if __name__ == '__main__':
    s = Solution()
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
             ]
    #matrix = [[1,3],[23,50]]
    target = 0
    print s.searchMatrix(matrix,target)