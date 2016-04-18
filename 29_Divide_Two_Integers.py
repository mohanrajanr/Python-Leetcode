class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        import sys
        maxint = 2147483647

        # What else will cause overflow?
        if divisor == 0:
            return maxint

        count = 0
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        res = 0

        while abs_dividend >= abs_divisor:
            sum_max = abs_divisor
            count = 1
            while sum_max + sum_max <= abs_dividend:
                sum_max += sum_max
                count += count
            abs_dividend -= sum_max
            res += count

        if (dividend > 0 > divisor) or (dividend < 0 < divisor):
            res = 0 - res
        return maxint if res > maxint else res

if __name__ == '__main__':
    s = Solution()
    dividend = -2147483648
    divisor = 1
    print s.divide(dividend, divisor)
