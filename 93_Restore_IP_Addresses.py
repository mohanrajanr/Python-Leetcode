# # # # -*- coding: utf-8 -*-
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, "", res)
        print (res)
        return res

    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return # backtracking
        for i in range(1, 4): # i represent the current index in s
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], index+1, path+s[0:i]+".", res)
                elif i == 2 and s[0] != '0':
                    self.dfs(s[i:], index+1, path+s[0:i]+".", res)
                elif i == 3 and s[0] != '0' and int(s[0:3]) <= 255:
                    self.dfs(s[i:], index+1, path+s[0:i]+".", res)


if __name__ == '__main__':
    s = Solution()
    ip = "1111"
    s.restoreIpAddresses(ip)
    