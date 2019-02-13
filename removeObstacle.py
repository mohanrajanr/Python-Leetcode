#!/usr/bin/python

# Date: 2018-07-25
#
# Description:
# You are in charge of preparing a recently purchased lot for one of amazon's
# new building. The lot is covered with trenches and has a single obstacle that
# needs to be taken down before the foundation can be prepared for the building.
# The demolition robot must remove the obstacle before progress can be made on
# the building.
# Write an algorithm to determine the minimum distance required for the
# demolition robot to remove the obstacle.
#
# Assumptions:
# 1. The lot is flat, except for trenches, and can be represented as a 2-D grid.
# 2. The demolition robot must start from top left corner of the lot, which is
#    always flat and can move one block up, down, right or left at a time.
# 3. The demolition robot cannot enter trenches and cannot leave the lot.
# 4. The flat areas are represented as 1, areas with trenches as 0 and
#    obstacle by 9.
#
# Output:
# Return an integer representing the minimum distance traversed to remove the
# obstacle else return -1.
#
# Approach:
# Sum of row_idx + column_idx where 9 is found will given minimum distance.
#
# Complexity:
# O(M*N)

def removeObstacle(numRows, numColumns, lot):
    """
    See shortestMazePath for more info. This is similar to shortestMazePath with
    slightly different conditions.

    1 <= numRows, numColumns <= 1000
    """

    possible_move =[
        [-1,0], # up
        [0,-1], # left
        [0,1], # right
        [1,0] # down
    ]
    x_min = y_min = 0
    x_max = numRows
    y_max = numColumns
    visited = [[0 for _ in range(y_max)] for _ in range(x_max)]
    visited[0][0] = 1

    queue = []
    # contains the point and distance, e.g. [1,1,2],
    # or [0,0,0] (because for origin [0,0] the distance is 0)
    queue.append([0,0,0])
    while len(queue) > 0:
        current_point = queue[0]
        if lot[current_point[0]][current_point[1]] == 9:
            return current_point[2]
        queue.pop(0)
        for i in range(0,4):
            next_x = current_point[0] + possible_move[i][0]
            next_y = current_point[1] + possible_move[i][1]
            if next_x >= 0 and next_y >= 0 and next_x < x_max and next_y < y_max:
                if (lot[next_x][next_y] == 1 or lot[next_x][next_y] == 9) and not visited[next_x][next_y]:
                    visited[next_x][next_y]=1
                    # putting each adjacent node into queue, meaning this is BFS
                    queue.append([next_x, next_y, current_point[2]+1])
    return -1

if __name__ == '__main__':
    lot = [
            [1,0,0],
            [1,0,0],
            [1,9,1]
            ]
    numRows = len(lot)
    numColumns = len(lot[0])
    assert removeObstacle(numRows, numColumns, lot) == 3

    lot = [
            [1,1,1,1],
            [0,1,1,1],
            [0,1,0,1],
            [1,1,9,1],
            [0,0,1,1]
            ]
    numRows = len(lot)
    numColumns = len(lot[0])
    assert removeObstacle(numRows, numColumns, lot) == 5

# Expected time complexity is O(MN).