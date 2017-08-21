# # # # -*- coding: utf-8 -*-

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Algorithm: binary search on first col, then binary search on the row
        m = len(matrix) # row
        n = len(matrix[0]) # col
        # binary search in matrix[row][0]
        firstColValues = [matrix[i][0] for i in xrange(m)]
        flag, row_location = self.binarySearch(firstColValues, target, 0, m-1)

        if not flag:
            flag, col_location = self.binarySearch(matrix[row_location], target, 0, n-1)

        return flag

    def binarySearch(self, array, target, start, end):
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
        if array[mid] < target:
            return False, mid
        return False, mid-1

if __name__ == '__main__':
    s = Solution()
    matrix = \
    [
  #[1,   4,  7, 11, 15],
  #[2,   5,  8, 12, 19],
  #[3,   6,  9, 16, 22],
  #[10, 13, 14, 17, 24],
  #[18, 21, 23, 26, 30]
        [20]
    ]
    #matrix = [[1,3],[23,50]]
    target = 20
    print s.searchMatrix(matrix,target)