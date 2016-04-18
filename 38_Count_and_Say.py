# # # -*- coding: utf-8 -*-
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
# 有没有可能在结果中出现大于3的数字?


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        # Note everytime the result will come from last result
        result = ""
        i = 0
        last_string = self.countAndSay(n-1)
        count = 1
        while i < len(last_string) - 1:
            if last_string[i] != last_string[i+1]:
                result += str(count)
                result += last_string[i]
                count = 1

            else:
                count += 1

            i += 1

        result += str(count)
        result += last_string[i]

        return result


if __name__ == '__main__':
    s = Solution()
    n = 6
    # for i in range(5):
    #     print s.countAndSay(i)
    print s.countAndSay(n)