# # # # -*- coding: utf-8 -*-
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i-1] * i
        print (fact)
        num = [str(i) for i in range(1,10)]
        result = ""
        k -= 1
        for i in range(n, 0, -1):
            j = k // fact[i-1]
            k = k % fact[i-1]
            result += num[j]
            num.pop(j)
        return result

if __name__ == '__main__':
    s = Solution()
    n = 4
    # nums = [i+1 for i in range(n)]
    # print nums
    #s.permute(n)
    # l1 = [1,2]
    # l2 = [3,4]
    # print l1+l2
    k = 17
    #print s.permutenums(n)
    print (s.getPermutation(n,k))