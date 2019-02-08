# -*- coding: utf-8 -*-


def shortestMazePath(maze, source, destination):
    """
    Given a MxN matrix where each element can either be 0 or 1.
    We need to find the shortest path between a given source cell to a
    destination cell. The path can only be created out of a cell if its value is 1.

    Expected time complexity is O(MN).

    For example –

    Input:
    mat[ROW][COL]  = {{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                      {1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
                      {1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
                      {0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
                      {1, 1, 1, 0, 1, 1, 1, 0, 1, 0 },
                      {1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
                      {1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                      {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                      {1, 1, 0, 0, 0, 0, 1, 0, 0, 1 }};
    Source = {0, 0};
    Destination = {3, 4};

    Output:
    Shortest Path is 11
    """
    if len(maze) == 0:
        return 0
    elif len(maze[0]) == 0:
        return 0

    possible_move =[
        [-1,0], # up
        [0,-1], # left
        [0,1], # right
        [1,0] # down
    ]
    x_min = y_min = 0
    x_max = len(maze)
    y_max = len(maze[0])
    visited = [[0 for _ in range(y_max)] for _ in range(x_max)]
    visited[0][0] = 1

    queue = []
    queue.append(source+[0]) # contains the point and distance, e.g. [1,1,2]
    while len(queue) > 0:
        current_point = queue[0]
        if current_point[0] == destination[0] and current_point[1] == destination[1]:
            return current_point[2]
        queue.pop(0)
        for i in range(0,4):
            next_x = current_point[0] + possible_move[i][0]
            next_y = current_point[1] + possible_move[i][1]
            if next_x >= 0 and next_y >= 0 and next_x < x_max and next_y < y_max:
                if maze[next_x][next_y] and not visited[next_x][next_y]:
                    visited[next_x][next_y]=1
                    # putting each adjacent node into queue, meaning this is BFS
                    queue.append([next_x, next_y, current_point[2]+1])
    return 0

if __name__ == '__main__':
    maze = [
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
            ]
    source = [0, 0]
    destination = [3, 4]
    print(shortestMazePath(maze, source, destination))
