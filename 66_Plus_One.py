# # # # -*- coding: utf-8 -*-
# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.
# 注意如何反转一个list! list.reverse() 的返回值是None
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def toNum(x,y):
            return x*10+y
        num = reduce(toNum,digits) + 1
        temp = []

        while num != 0:
            digit = num % 10
            temp.append(digit)
            num /= 10
        # print temp[::-1]
        # print temp.reverse()
         # print temp
        return temp[::-1]

if __name__ == '__main__':
    s = Solution()
    digits = [9,9,9]
    print s.plusOne(digits)
