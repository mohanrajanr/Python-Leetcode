# # # # -*- coding: utf-8 -*-
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = []
        coins = sorted(coins, reverse=True)
        self.dfs(coins, amount, [], res)
        print(res)
        if len(res) > 0:
            return len(res[0])
        return -1

    def dfs(self, coins, amount, path, res):
        if amount < 0:
            return
        if amount == 0:
            res.append(path)
            return
        for c in coins:
            if c <= amount:
                next_amount = amount - c
                self.dfs(coins, next_amount, path+[c], res)

if __name__ == '__main__':
    s = Solution()
    coins = [5,2,1]
    amount = 11
    print(s.coinChange(coins, amount))
    