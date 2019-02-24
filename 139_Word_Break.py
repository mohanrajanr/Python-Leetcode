# # # # -*- coding: utf-8 -*-
class Solution(object):
    memory = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s in self.memory:
            return True

        wordDict = set(wordDict)

        if len(s) == 0:
            return True
        for i in range(0, len(s)):
            current_string = s[0:i+1]
            if current_string in wordDict:
                self.memory[current_string] = True
                sub_string = s[i+1:]
                if self.wordBreak(sub_string, wordDict):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    word = "applepenapple"
    wordDict = ["apple", "pen"]
    word = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    word = "a"
    wordDict = ["b"]
    print(s.wordBreak(word, wordDict))