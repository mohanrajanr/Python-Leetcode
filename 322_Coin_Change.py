# # # # -*- coding: utf-8 -*-
import sys
class Solution(object):
    res = sys.maxint

    # def coinChange(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #     n = len(coins)
    #     self.helper(coins, n-1, amount, 0)
    #     if self.res == sys.maxint:
    #         return -1
    #     else:
    #         return self.res
    #
    # def helper(self, coins, start, amount, cur):
    #     if amount < 0:
    #         return
    #     if amount == 0:
    #         self.res = min(self.res, cur)
    #         return
    #     for i in range(start, -1, -1):
    #         self.helper(coins, i, amount-coins[i], cur+1)


if __name__ == '__main__':
    s = Solution()
    coins = [5,2,1]
    amount = 11
    print(s.coinChange(coins, amount))
    