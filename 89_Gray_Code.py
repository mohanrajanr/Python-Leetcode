# # # # -*- coding: utf-8 -*-
class Solution:
    def grayCode(self, n):
        ret = [0]
        for k in range(0, n):
            for i in range(len(ret)-1, -1, -1):
                ret.append(ret[i]+(2**k))
        return ret

if __name__ == '__main__':
    s = Solution()
    s.grayCode(3)
