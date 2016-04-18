# # # # -*- coding: utf-8 -*-
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        start = 0
        end = x
        mid = (start + end) / 2
        while start <= mid < end:
            val = pow(mid,2)
            if val > x:
                end = mid
                mid = (start+end)/2
            elif val < x:
                if pow(mid+1,2) > x:
                    return mid
                else:
                    start = mid
                    mid = (start+end)/2
            else:
                return mid
        return mid

class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        half = x / 2
        while pow(half,2) > x:
            half /= 2

        for i in xrange(half,half*2):
            if pow(i,2) <= x and pow(i+1,2) > x:
                return i
        return

if __name__ == '__main__':
    s = Solution()
    x = 1
    print s.mySqrt(x)
    