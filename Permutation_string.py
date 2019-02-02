# # # # -*- coding: utf-8 -*-
class Solution:
    def permutation(self, str):
        """

        :param str:
        :return: list[str]
        """
        res = []
        self.dfs(str, "", res)
        return res

    def dfs(self, str, temp, res):
        if len(str) == 0:
            res.append(temp)
        for i in range(0, len(str)):
            others = str[0:i]+str[i+1:]
            self.dfs(others, temp+str[i], res)

if __name__ == '__main__':
    s = Solution()
    str = 'abc'
    print(s.permutation(str))