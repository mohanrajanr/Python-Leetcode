# # -*- coding: utf-8 -*-
# 根据解题本质发展出来的解题方法有二种
# 摒除法
# 1.摒除法：用数字去找单元内唯一可填空格，称为摒除法，数字可填唯一空格称为摒余解(隐性唯一解)。
# 根据不同的作用范围，摒余解可分为下述三种：
# 1.1 数字可填唯一空格在「宫」单元称为宫摒余解(Hidden Single in Box)，这种解法称宫摒除法。
# 1.2 数字可填唯一空格在「行」单元称为行摒余解(Hidden Single in Row)，这种解法称行摒除法。
# 1.3 数字可填唯一空格在「列」单元称为列摒余解(Hidden Single in Column)，这种解法称列摒除法。
# 1.4 行摒余解和列摒余解合称行列摒余解(Hidden Single in Line)。
# 1.5 得到行列摒余解的方法称为行列摒除法。
# 余数法
# 2.余数法：用格位去找唯一可填数字，称为余数法，格位唯一可填数字称为唯余解(Naked Single)。
# 余数法是删减等位群格位(Peer)已出现的数字的方法，每一格位的等位群格位有 20 个，如图七所示。
# 辅助解法
# 3.上述方法称为基础解法(Basic Techinques)，其他所有的解法称为进阶解法(Advanced Techniques)，是在补基本解法之不足，所以又称辅助解法。

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

if __name__ == '__main__':
    s = Solution()
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    s.solveSudoku(board)