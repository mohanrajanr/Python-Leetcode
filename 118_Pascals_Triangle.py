# # # # -*- coding: utf-8 -*-
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        result.append([1])
        for i in range(1, numRows):
            l = [1 for x in range(i+1)]
            last_l = result[i-1]

            for j in range(1,i):
                l[j] = last_l[j] + last_l[j-1]
            result.append(l)

        #print result
        return result

if __name__ == '__main__':
    s = Solution()
    numRows = 5
    print s.generate(numRows)