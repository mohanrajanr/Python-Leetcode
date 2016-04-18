# # # # -*- coding: utf-8 -*-
# 关于N-queens的回溯算法: http://www.acmerblog.com/n-queen-3411.html
#
# 参考解法:
# 1. http://chaoren.is-programmer.com/posts/43589.html
# 2. http://www.acmerblog.com/n-queen-3411.html
# 把棋盘存储为一个N维数组board[N]，数组中第i个元素的值代表第i行的皇后位置，这样便可以把问题的空间规模压缩为一维O(N)，
# 在判断是否冲突时也很简单，首先每行只有一个皇后，且在数组中只占据一个元素的位置，行冲突就不存在了，其次是列冲突，
# 判断一下是否有board[i]与当前要放置皇后的列j相等即可。至于斜线冲突，通过观察可以发现所有在斜线上冲突的皇后的位置都有规律,
# 即它们所在的行列互减的绝对值相等，即|row – i | = | col – board[i] | 。这样某个位置是否可以放置皇后的问题已经解决。


class Solution(object):
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.res = []
        # board在这里初始化
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res

    def solve(self, n, row, board):
        # row为n,说明此时board已经被填充n-1个元素, 已填满
        if row == n:
            oneAnswer = [ ['.' for j in xrange(n)] for i in xrange(n) ]
            for i in xrange(n):
                # at row i, col board[i], this is a good placement of Queen
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.res.append(oneAnswer)
            return

        # 对列col进行扫描
        for col in xrange(n):
            if self.isValid(board, col, row):
                board[row] = col
                # print board
                # 每次都往下探测下一行
                self.solve(n, row + 1, board)

    def isValid(self, board, col, row):
        valid = True
        # 只需要判断row前面的行，因为后面的行还没有放置
        for i in xrange(row):
            # col是待放置的位置,如果在board的值中 (board[i])已经有这个col,说明col冲突了
            if board[i] == col:
                valid = False
                break
            # check dianogal
            if abs(board[i] - col) == row - i:
                valid = False
                break
        return valid


class Solution1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = self.generatePermutationByNum(n)
        ret = []
        for coordinate in result:
            if self.checkifondiagonal(coordinate):
                ret.append(self.buildMatrix(coordinate))
        return ret

    def buildMatrix(self, coordinate):
        matrix = []
        n = len(coordinate)
        for i in range(n):
            dot_string = ""
            y = int(coordinate[i])
            for j in range(n):
                if j == y:
                    dot_string += 'Q'
                else:
                    dot_string += "."
            matrix.append(dot_string)
        return matrix

    def checkifondiagonal(self, coordinate):
        """
        :type coordinate: str
        :rtype: Boolean
        """
        # Coordinate example: "012"
        for i in range(len(coordinate)):
            for j in range(i+1,len(coordinate)):
                x_diff = j-i
                y_diff = abs(int(coordinate[i]) - int(coordinate[j]))
                # if x_diff == y_diff, they are on diagonal, so it's not a valid input, we should return False
                if x_diff == y_diff:
                    return False
        return True

    def generatePermutationByNum(self, n):
        num_lst = [str(i) for i in range(n)]
        result = self.generatePermutation(num_lst)
        return result

    def generatePermutation(self, num_lst):
        if not num_lst:
            return ['']
        if len(num_lst) == 1:
            return [num_lst[0]]

        result = []
        for i in range(0,len(num_lst)):
            for item in self.generatePermutation(num_lst[0:i]+num_lst[i+1:]):
                temp = num_lst[i] + item
                result.append(temp)
        return result

if __name__ == '__main__':
    s = Solution()
    n = 4
    print s.solveNQueens(n)
    