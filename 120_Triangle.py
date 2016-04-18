# # # # -*- coding: utf-8 -*-
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# 关于二叉树的小结:
# http://blog.csdn.net/sunmenggmail/article/details/7466635
# 然而此题不是用二叉树..举例:
# [2],
# [3,4],
# [5,6,7],
# [8,9,10,11]

# 可生成二维矩阵,每个点记录从上一层的节点到本层(左右两个)节点的和
# [2]
# [5,6]
# [10,11,12,13]
# [18,19,20,21,22,23,24,25]

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        n = len(triangle)
        result = []
        result.append(triangle[0][0])
        import copy
        for i in range(1,n):
            last_row = copy.deepcopy(result)
            result = []
            for j in range(len(triangle[i])):
                if j == 0:
                    val = last_row[0] + triangle[i][0]
                elif j == len(triangle[i])-1:
                    val = last_row[-1] + triangle[i][j]
                else:
                    val = min(last_row[j-1],last_row[j]) + triangle[i][j]
                result.append(val)
            #print result
        return min(result)

class Solution1(object):
    def minimumTotal(self, triangle):
        self.res = []
        self.path = []
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.visit(0,0,len(triangle),triangle)
        return min(self.res)

    #问题：打印二叉树中的所有路径
    def visit(self,i,j,n,triangle,path=None):
        if path is None:
            path = []
        path.append([i,j])
        if i == n-1:
            print path
            # self.res.append(path)
            curr_sum = 0
            for coordinate in path:
                curr_sum += triangle[coordinate[0]][coordinate[1]]
            # print curr_sum
            self.res.append(curr_sum)
        else:
            self.visit(i+1,j,n,triangle,path)
            path.pop()
            self.visit(i+1,j+1,n,triangle,path)
            path.pop()



if __name__ == '__main__':
    s = Solution()
    triangle =  [
                    [2],
                   [3,4],
                  [6,5,7],
                 [4,1,8,3]
                ]
    print s.minimumTotal(triangle)
    