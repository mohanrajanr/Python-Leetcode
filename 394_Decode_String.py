# # # # -*- coding: utf-8 -*-
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currNum = 0
        currStr = ''
        result = ''
        for character in s:
            if character.isdigit():
                currNum = currNum * 10 + int(character)
            elif character.isalpha():
                currStr += character
            elif character == '[':
                if currStr:
                    stack.append(currStr)
                    currStr = ''
                if currNum != 0:
                    stack.append(currNum)
                    currNum = 0
            elif character == ']':
                lastNum = stack.pop()
                lastStr = stack.pop()
                lastResult = lastStr + lastNum * currStr
                lastStr = stack.pop()
                stack.append(lastStr + lastResult)

if __name__ == '__main__':
    s = Solution()
    test_str = '3[a2[c]]'