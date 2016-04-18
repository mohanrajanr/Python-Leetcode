# # # # -*- coding: utf-8 -*-
# http://www.cnblogs.com/flowerkzj/p/3726667.html
# DP(i, j)存的是p[0:i-1]与s[0:j-1]的匹配情况。
# DP(i+1, j+1)是要更新的状态，对应p[i]和s[j]
# 1. 当p[i] 的下一个不为'*'时，此时只跟上一个状态的p与上一个s对应的DP(i, j)有关
# 　因为此时匹配的条件是：A. p[i]与s[j]匹配。B. p[0:i-1]与s[0:j-1]完全匹配，即DP(i, j)==true。
# 　则
# 　　　　DP(i+1, j+1) = DP(i, j) && Match(p[i], s[j])
# 　另外考虑DP(i+1, 0)，这个值对应的是s[-1]与p[i]，s[-1]即假设存在的空字符，明显p[i]与s[-1]是不匹配的
#    因此这时的DP(i+1, 0) = false
# 　而要让规划顺利地开始，（特别是当第一个匹配对的就是这种情况时）就需要让DP(0, 0)=true了。
#
# 2. 当p[i]的下一个为'*'时，此时就与围绕这一状态的都有关。
# 　　1) 如果DP(i, j+1)是true时，即上一个pattern就已经完全匹配了当前的s，那当前状态也应该是true，即DP(i+1, j+1)=true
# 　　2) 否则，DP(i, j)与DP(i+1, j)其中有一个为true, 而且p[i]与s[j]匹配，则DP(i+1, j+1)为true，即
# 　　　　DP(i+1, j+1) = (DP(i, j) || DP(i+1, j)) && Match(p[i], s[j])
# 　此时考虑DP(i+1, 0)则需要DP(i, 0)的配合，DP(i+1, 0) = DP(i, 0) && Match(p[i], s[-1])
# 　而Match(p[i], s[-1])永远为真，所以DP(i+1, 0) = DP(i, 0)
# 另外考虑到匹配情况只跟相邻两层有关，所以实现时就只用了两层存状态。

class Solution(object):
    def isMatch(self, s, p):
        # https://leetcode.com/discuss/55253/my-dp-approach-in-python-with-comments-and-unittest
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        # for meaning of "_" , check http://python.jobbole.com/81129/
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]
        print table
        return table[-1][-1]

if __name__ == '__main__':
    s = Solution()
    source = 'aab'
    target = 'a*a*b'
    print s.isMatch(source,target)
    #print 0 |= 1
