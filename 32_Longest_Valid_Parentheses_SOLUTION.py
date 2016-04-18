# -*- coding: utf-8 -*-
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxlen = 0
        stack = []  # 创建一个stack用来保存左括号
        last = -1  # 用last 标记很巧妙 - 当找到一个右括号,栈中却没有左括号时,就更新下次evaluate的位置
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    # 没有匹配上，来了一个右括号却没有左括号匹配就刷新last的位置
                    last = i
                else:
                    # 找到匹配的时候才需要计算最大长度

                    # 找到匹配了，就pop一个最近的左括号的index
                    stack.pop()
                    if stack == []:
                        # 如果空了，就看看跟last就是第一个左括号的距离
                        maxlen = max(maxlen, i - last)
                    else:
                        # 如果不空，用peek找到最近的左括号的index-1;
                        # stack[len(stack)-1] 是stack栈顶的左括号的index
                        maxlen = max(maxlen, i - stack[len(stack) - 1])
        return maxlen


if __name__ == '__main__':
    s = Solution()

    str = ')(((())()))'
    print s.longestValidParentheses(str)
