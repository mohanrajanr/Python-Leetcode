# # # # -*- coding: utf-8 -*-
"""
Given an array of words, e.g. ["ab", "cd", "ef"], return all possible combinations
by picking up one character from each word.

["ace", "acf", "ade", "adf", "bce", "bcf", "bde", "bdf"]
"""

class Solution(object):
    def combine(self, words):
        res = []
        self.dfs(words, 0, "", res)
        return res

    def dfs(self, words, index, curr, res):
        if len(curr) == len(words):
            res.append(curr)
            return
        for i in xrange(index, len(words)):
            word = words[i]
            for c in word:
                self.dfs(words, i+1, curr+c, res)

if __name__ == '__main__':
    s = Solution()
    words = ["ab", "cd", "ef"]
    print(s.combine(words))