# # # # -*- coding: utf-8 -*-

# 一直都要用边界来限制i,j i和j的值不能记录上次的状态
# 用for循环!
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = []

        # if m == 1:
        #     return matrix[0]
        # elif n == 1:
        #     for i in range(0,m):
        #         result.append(matrix[i][0])
        #     return result

        right_edge = n-1
        left_edge = 0
        top_edge = 0
        bottom_edge = m-1
        i, j = 0, 0
        while right_edge > left_edge and bottom_edge > top_edge:
            ### Use for loop, because we need to reset j and i starting point!
            # i = top_edge
            # j = left_edge
            for j in range(left_edge,right_edge):
            #while j < right_edge:
                #result.append(matrix[i][j])
                result.append(matrix[top_edge][j])
            #top_edge = top_edge + 1 if top_edge < bottom_edge else top_edge
            for i in range(top_edge,bottom_edge):
            #while i < bottom_edge:
                result.append(matrix[i][right_edge])
            #right_edge = right_edge - 1 if right_edge > left_edge else right_edge
            for j in range(right_edge,left_edge,-1):
            #while j > left_edge:
                result.append(matrix[bottom_edge][j])
            #bottom_edge = bottom_edge - 1 if bottom_edge > top_edge else bottom_edge
            for i in range(bottom_edge,top_edge,-1):
            #while i > top_edge:
                result.append(matrix[i][left_edge])
            #left_edge = left_edge + 1 if left_edge < right_edge else left_edge

            # Note bottom_edge could be smaller than top_edge!!!
            # top_edge = top_edge + 1 if top_edge < bottom_edge else top_edge
            # right_edge = right_edge - 1 if right_edge > left_edge else right_edge
            # bottom_edge = bottom_edge - 1 if bottom_edge > top_edge else bottom_edge
            # left_edge = left_edge + 1 if left_edge < right_edge else left_edge
            top_edge += 1
            right_edge -= 1
            bottom_edge -= 1
            left_edge += 1

            # if bottom_edge == top_edge or right_edge == left_edge:
            #     break

        if bottom_edge == top_edge and right_edge == left_edge:
            #return result
            result.append(matrix[bottom_edge][left_edge])
        elif bottom_edge == top_edge:
            for j in range(left_edge,right_edge+1):
                result.append(matrix[top_edge][j])
        elif left_edge == right_edge:
            for i in range(top_edge,bottom_edge+1):
                result.append(matrix[i][right_edge])

        return result

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    #matrix = [[1,2,3],[4,5,6],]
    #matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16],[17,18,19,20]]
    #matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16],]

    print s.spiralOrder(matrix)