# # # # -*- coding: utf-8 -*-
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c]) # j 是当前字符往前的最大位置
            if i == j: # 说明已经到达当前某个字符串末尾的最大区间
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans

if __name__ == '__main__':
    s = Solution()
    text = 'ababcbacadefegdehijhklij'
    s.partitionLabels(text)