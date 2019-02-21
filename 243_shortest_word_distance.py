# # # # -*- coding: utf-8 -*-

"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

"""

"""
我们其实需要遍历一次数组就可以了，我们用两个变量p1,p2初始化为-1，
然后我们遍历数组，遇到单词1，就将其位置存在p1里，若遇到单词2，
就将其位置存在p2里，如果此时p1, p2都不为-1了，那么我们更新结果
"""

class Solution:
    def shortestWordDistance(self, words, word1, word2):
        import sys
        p1, p2 = -1, -1
        minimum_distance = sys.maxint
        for i in range(len(words)):
            if words[i] == word1:
                if p1 == -1:
                    p1 = i
                else:
                    if minimum_distance > abs(p1-p2):
                        p1 = i
                        minimum_distance = abs(p1-p2)
            elif words[i] == word2:
                if p2 == -1:
                    p2 = i
                else:
                    if minimum_distance > abs(p1-p2):
                        p2 = i
                        minimum_distance = abs(p1-p2)
        return min(minimum_distance, abs(p1-p2))

if __name__ == '__main__':
    s = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    assert s.shortestWordDistance(words, word1, word2) == 3

    word1 = "makes"
    word2 = "coding"
    assert s.shortestWordDistance(words, word1, word2) == 1