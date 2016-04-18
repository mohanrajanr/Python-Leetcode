# # # # -*- coding: utf-8 -*-
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a) - 1
        n = len(b) - 1
        result = ""
        carry = 0

        while m >= 0 and n >= 0:
            curr_digit = int(a[m]) + int(b[n]) + carry # 0,1,2,3
            if curr_digit >= 2:
                carry = 1
            else:
                carry = 0

            curr_digit %= 2
            result += str(curr_digit)

            m -= 1
            n -= 1

        if n < 0:
            while m >= 0:
                curr_digit = int(a[m]) + carry
                if curr_digit >= 2:
                    carry = 1
                else:
                    carry = 0
                curr_digit %= 2
                result += str(curr_digit)
                m -= 1
        elif m < 0:
            while n >= 0:
                curr_digit = int(b[n]) + carry
                if curr_digit >= 2:
                    carry = 1
                else:
                    carry = 0
                curr_digit %= 2
                result += str(curr_digit)
                n -= 1
        if carry > 0:
            result += str(carry)

        return result[::-1]

if __name__ == '__main__':
    s = Solution()
    a = "11"
    b = "11111"
    print s.addBinary(a,b)