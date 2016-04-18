# # # # -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 or len(num2) == 0:
            return ""

        num1_number = int(num1)
        num2_number = int(num2)

        result = num1_number * num2_number

        return str(result)
if __name__ == '__main__':
    s = Solution()
    num1 = '-20'
    num2 = '400'
    print s.multiply(num1,num2)
    