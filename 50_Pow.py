# # # # -*- coding: utf-8 -*-
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        # This line is important!! Note x^-n = (1/x)^n
        if n < 0:
            n = -n
            x = 1/x
        if n % 2 == 0:
            return self.myPow(x*x,n/2)
        else:
            return x*self.myPow(x*x,n/2)

if __name__ == '__main__':
    s = Solution()
    x = 2.0
    n = -4
    print s.myPow(x,n)