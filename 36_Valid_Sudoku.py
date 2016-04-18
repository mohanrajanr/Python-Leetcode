# -*- coding: utf-8 -*-
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Question 1. how to judge if a string that contains "." ("." can be single char wildcard)
        # and the rest numbers are in 1~9, each show up once?

        # Question 2. how to get all 9 numbers for: 1) one column 2) one row 3) one square

        # validate each row
        for num_str in board:
            if not self.isStrValidForSudoku(num_str):
                return False

        for i in range(0, 9):
            column_str = ""
            for j in range(0, 9):
                column_str += board[j][i]
            if not self.isStrValidForSudoku(column_str):
                return False

        row = 0
        square_str = ""
        while row < 9:
            column = 0
            while column < 9:
                square_str = ""
                for i in range(row, row + 3):
                    for j in range(column, column + 3):
                        square_str += board[i][j]
                if not self.isStrValidForSudoku(square_str):
                    return False
                #print square_str
                column += 3
            row += 3

                # [0][0], [0][1], [0][2]
                # [1][0], [1][1], [1][2]
                # [2][0], [2][1], [2][2]

                # [3][0],[3][1],[5][2]
                # [4][0],[4][1],[4][2]
                # [5][0],[5][1],[3][2]
        return True

    def isStrValidForSudoku(self, s):
        """
        :param s: str
        :return: bool
        """
        number_dict = {'1': 0,
                       '2': 0,
                       '3': 0,
                       '4': 0,
                       '5': 0,
                       '6': 0,
                       '7': 0,
                       '8': 0,
                       '9': 0,
                       }

        for current_char in s:
            if current_char in number_dict.keys():

                if number_dict[current_char] >= 1:
                    return False
                else:
                    number_dict[current_char] += 1

            elif current_char == '.':
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    board = [".87654321", "21.......", "3........", "4........", "5........", "6........", "7........", "8........",
             "9........"]
    board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    for i in board:
        print i
    #board = [".........", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789"]
    num_str = "1.2345678"
    # print s.isStrValidForSudoku(num_str)
    print s.isValidSudoku(board)
