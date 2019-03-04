# # # # -*- coding: utf-8 -*-
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        # Below is incorrect!!! because columns are the same list that copied three times
        # columns = [' ' for _ in range(n)]
        # self.matrix = [columns for _ in range(n)]
        self.matrix = [[' ' for _ in range(n)] for _ in range(n)]

    def checklst(self, lst):
        X_exists = False
        O_exists = False
        E_exists = False

        if 'X' in lst:
            X_exists = True
        if 'O' in lst:
            O_exists = True
        if ' ' in lst:
            E_exists = True

        if X_exists and not O_exists and not E_exists:
            return True, 1
        elif O_exists and not X_exists and not E_exists:
            return True, 2
        else:
            return False, 0

    def checkWins(self):
        for i in range(self.n):
            row = self.matrix[i] # 0 based
            is_win, who = self.checklst(row)
            if is_win:
                return who

            column = [row[i] for row in self.matrix]
            is_win, who = self.checklst(column)
            if is_win:
                return who

        lst_diagonal = [self.matrix[i][i] for i in range(self.n)]
        lst_rev_diagonal = [self.matrix[i][self.n-i-1] for i in range(self.n)]
        is_win, who = self.checklst(lst_diagonal)
        if is_win:
            return who
        is_win, who = self.checklst(lst_rev_diagonal)
        if is_win:
            return who
        return 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            self.matrix[row][col] = 'X'
        elif player == 2:
            self.matrix[row][col] = 'O'

        return self.checkWins()


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

if __name__ == '__main__':
    toe = TicTacToe(3)
    toe.move(0, 0, 1)
    toe.move(0, 2, 2)
    toe.move(2, 2, 1)
    toe.move(1, 1, 2)
    toe.move(2, 0, 1)
    toe.move(1, 0, 2)
    toe.move(2, 1, 1)
    