from os import *
from sys import *
from collections import *
from math import *


def isSafe(x, y, n, visited, maze):
    if (0 <= x < n) and (0 <= y < n) and (visited[x][y] == 0) and (maze[x][y] == 1):
        return True
    return False


def solve(maze, n, ans, x, y, moves, visited):
    # Base case
    if x == n - 1 and y == n - 1:
        visited[x][y] = 1
        temp = []
        for i in range(n):
            for j in range(n):
                temp.append(visited[i][j])
        visited[x][y] = 0
        ans.append(temp)
        return
    visited[x][y] = 1

    # down
    newx = x + 1
    newy = y
    if isSafe(newx, newy, n, visited, maze):
        solve(maze, n, ans, newx, newy, moves, visited)

    # left
    newx = x
    newy = y - 1
    if isSafe(newx, newy, n, visited, maze):
        solve(maze, n, ans, newx, newy, moves, visited)

    # right
    newx = x
    newy = y + 1
    if isSafe(newx, newy, n, visited, maze):
        solve(maze, n, ans, newx, newy, moves, visited)

    # up
    newx = x - 1
    newy = y
    if isSafe(newx, newy, n, visited, maze):
        solve(maze, n, ans, newx, newy, moves, visited)

    visited[x][y] = 0


def ratInAMaze(maze, n):
    ans = []
    if maze[0][0] == 0:
        return ans

    moves = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    solve(maze, n, ans, 0, 0, moves, visited)
    return ans


# Main.
n = int(input())
maze = [0] * n

for i in range(n):
    maze[i] = input().split()
    maze[i] = [int(j) for j in maze[i]]

result = ratInAMaze(maze, n)
for ul in result:
    for li in ul:
        print(li, end=" ")
    print()
