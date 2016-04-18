# # # # -*- coding: utf-8 -*-

# 一直都要用边界来限制i,j i和j的值不能记录上次的状态
# 用for循环!

class Solution(object):


    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #Creates the number list
        max_num = pow(n,2)
        nums = [x for x in range(1,max_num+1)]
        #Init matrix and set all values to 0
        matrix = [[0 for x in range(n)] for x in range(n)]

        l = 0
        r = n-1
        t = 0
        b = n-1

        index = 0
        while r > l and b > t:
            for i in range(l,r):
                matrix[t][i] = nums[index]
                index += 1
            for i in range(t,b):
                matrix[i][r] = nums[index]
                index += 1
            for i in range(r,l,-1):
                matrix[b][i] = nums[index]
                index += 1
            for i in range(b,t,-1):
                matrix[i][l] = nums[index]
                index += 1

            l += 1
            r -= 1
            t += 1
            b -= 1
        if l == r and t == b:
            matrix[t][l] = nums[index]
            return matrix
        elif l == r:
            for i in range(t,b+1):
                matrix[i][l] = nums[index]
                index += 1
        elif t == b:
            for i in range(l,r+1):
                matrix[t][i] = nums[index]
                index += 1
        return matrix

if __name__ == '__main__':
    s = Solution()
    n = 10
    print s.generateMatrix(n)
