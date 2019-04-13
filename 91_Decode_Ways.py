# # # # -*- coding: utf-8 -*-
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        for i in range(65, 65+26):
            hashmap[str(i-64)] = chr(i)
        print (hashmap) #
        # create
        # {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H',
        #  '9': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P',
        #  '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X',
        #  '25': 'Y', '26': 'Z'}
        res = []
        self.dfs(s, 0, res, hashmap, [])
        return res

    def dfs(self, s, start, res, hashmap, path):
        if start == len(s):
            res.append(path[:])
            return
        for i in range(start, len(s)):
            if s[start] in hashmap:
                path.append(hashmap[s[start]])
                self.dfs(s, start+1, res, hashmap, path)
                path.remove(hashmap[s[start]])
            if start+2 < len(s) and s[start:start+2] in hashmap:
                path.append(hashmap[s[start:start+2]])
                self.dfs(s, start+2, res, hashmap, path)
                path.remove(hashmap[s[start:start+2]])


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('12'))
