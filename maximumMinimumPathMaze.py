# # # # -*- coding: utf-8 -*-
"""
/*
Maximum Minimum Path
给一个int[][]的matirx，对于一条从左上到右下的path p_i，p_i中的最小值是m_i，求所有m_i中的最大值。只能往下或右
比如：
[8, 4, 7]
[6, 5, 9]
有3条path：
8-4-7-9 min: 4
8-4-5-9 min: 4
8-6-5-9 min: 5
return: 5.
*/


public static int maximumMinimumPath(int[][] matrix) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
        return 0;
    }
    int n = matrix.length;
    int m = matrix[0].length;
    int[][] dp = new int[n][m];                                // dp[i,j]路径中最小值 (不过下边有所不同)
    dp[0][0] = matrix[0][0];// [0,0] 肯定在考虑点中
    for (int i = 1; i < n; i++) {
        dp[i][0] = Math.min(dp[i - 1][0], matrix[i][0]);
    }
    for (int i = 1; i < m; i++) {
        dp[0][i] = Math.min(dp[0][i - 1], matrix[0][i]);
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            dp[i][j] = Math.min(Math.max(dp[i - 1][j], dp[i][j - 1]),// 每次选点的时候,因为路径只可能是从上或者从左, 所以选其中较大的, 再去合当前值比较.即可
                    matrix[i][j]);
        }
    }
    return dp[n - 1][m - 1];
}

public static void main(String[] args) {
    int[][] d = new int[][]{
            {8,4,3,5},
            {6,5,9,8},
            {7,2,3,6}
    } ;
    System.out.println(maximumMinimumPath(d)); // 5
}
"""


def maximumMinimumPath(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = matrix[0][0]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], matrix[i][0])
    for i in range(1, m):
        dp[0][i] = min(dp[0][i-1], matrix[0][i])
    for i in range(1, n):
        for j in range(1, m):
            curr_max = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = min(matrix[i][j], curr_max)
    return dp[n-1][m-1]

if __name__ == '__main__':
    matrix = [[8, 4, 7],
              [6, 5, 9]
              ]
    print(maximumMinimumPath(matrix))

# O(m*n)