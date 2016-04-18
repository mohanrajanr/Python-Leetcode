class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        # result = 0
        # for i in range(1, len(s)):
        #     if s[i-1] == "(" and s[i] == ")":
        #         result += 2
        #     s = s[0:i-1]+s[i+1:]
        #     print s
        #     result += self.longestValidParentheses(s)
        # return result

        """
        # Below is considering when ")(" happens then it should be reevaluated
        l = []
        index = 0
        result = 0
        max_length = 0
        if s[index] == '(':
            l.append(index)
            index += 1

        while index < len(s):
            if s[index] == ')':
                if len(l) > 0:
                    l.pop()
                    result += 2
                else:
                    max_length = result if result > max_length else max_length
                    while len(l) > 0:
                        l.pop()

                    result = 0
            elif s[index] == '(':
                if s[index - 1] == ')':
                    max_length = result if result > max_length else max_length

                    result = 0
                    while len(l) > 0:
                        l.pop()

                l.append(index)
            index += 1

        max_length = result if result > max_length else max_length

        return max_length
        """

        l = []
        index = 0
        result = 0
        max_length = 0
        while index < len(s):
            if s[index] == ')':
                if len(l) > 0:
                    l.pop()
                    result += 2
                else:
                    max_length = result if result > max_length else max_length
                    result = 0
            elif s[index] == '(':
                l.append(index)
            index += 1

        max_length = result if result > max_length else max_length
        return max_length

if __name__ == '__main__':
    s = Solution()

    str = ')(((())()))'
    print s.longestValidParentheses(str)