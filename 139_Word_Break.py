# # # # -*- coding: utf-8 -*-
class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s, wordDict, 0, {})

    def helper(self, s, wordDict, start, temp):
        if start == len(s):
            return True
        if start in temp:
            return temp[start]
        for i in range(start+1, len(s)+1):
            sub_string = s[start:i]
            if sub_string in wordDict and self.helper(s, wordDict, i, temp):
                temp[start] = True
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    word = "applepenapple"
    wordDict = ["apple", "pen"]
    # word = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # word = "a"
    # wordDict = ["b"]
    print(s.wordBreak(word, wordDict))