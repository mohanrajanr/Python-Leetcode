# # # # -*- coding: utf-8 -*-

def find_path_dfs(maze):
    start = [0, 0]
    goal = [len(maze) - 1, len(maze[0]) - 1]
    stack = []
    stack.append(start+[0])

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
    visited[0][0] = 1 # mark as visited

    while len(stack) > 0:
        current = stack.pop()
        if current[0] == goal[0] and current[1] == goal[1]:
            return current[2]
        if visited[current[0]][current[1]]:
            continue
        visited[current[0]][current[1]] = 1
        for i in range(0,4):
            next_x = current[0] + possible_move[i][0]
            next_y = current[1] + possible_move[i][1]
            if next_x >= 0 and next_y >= 0 and next_x < x_max and next_y < y_max:
                stack.append([next_x, next_y, current[2]+1])
    return -1
