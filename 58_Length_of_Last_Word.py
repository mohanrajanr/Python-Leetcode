# # # # -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i = len(s) - 1
        length = 0
        # return the length of last word in the string
        while s[i] == ' ':
            # length += 1
            i -= 1
            if i < 0:
                return 0

        while s[i] != ' ':
            length += 1
            i -= 1
            if i < 0:
                return length
        return length


if __name__ == '__main__':
    s = Solution()
    str = "  abb bb aaaaaaa"
    #str = "    "

    print s.lengthOfLastWord(str)