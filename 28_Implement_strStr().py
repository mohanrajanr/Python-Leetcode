class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or haystack is None or (len(needle) > len(haystack)):
            return -1

        for i in range(0,len(haystack)-len(needle)+1):
            j = 0
            while j < len(needle):
                if needle[j] != haystack[j+i]:
                    break;
                j += 1

            if j == len(needle):
                return i

        return -1

if __name__ == '__main__':
    s = Solution()
    haystack = "bbbbbbabcsssd"
    needle = "abcssssssssss"
    print s.strStr(haystack,needle)