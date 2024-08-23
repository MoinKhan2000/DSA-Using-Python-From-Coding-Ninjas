""" 
Rat in a Maze
Send Feedback
You are given a starting position for a rat which is stuck in a maze at an initial point (0, 0) (the maze can be thought of as a 2-dimensional plane). The maze would be given in the form of a square matrix of order 'N' * 'N' where the cells with value 0 represent the maze’s blocked locations while value 1 is the open/available path that the rat can take to reach its destination. The rat's destination is at ('N' - 1, 'N' - 1). Your task is to find all the possible paths that the rat can take to reach from source to destination in the maze. The possible directions that it can take to move in the maze are 'U'(up) i.e. (x, y - 1) , 'D'(down) i.e. (x, y + 1) , 'L' (left) i.e. (x - 1, y), 'R' (right) i.e. (x + 1, y).
Note:
Here, sorted paths mean that the expected output should be in alphabetical order.
For Example:
Given a square matrix of size 4*4 (i.e. here 'N' = 4):
1 0 0 0
1 1 0 0
1 1 0 0
0 1 1 1 
Expected Output:
DDRDRR DRDDRR 
i.e. Path-1: DDRDRR and Path-2: DRDDRR

The rat can reach the destination at (3, 3) from (0, 0) by two paths, i.e. DRDDRR and DDRDRR when printed in sorted order, we get DDRDRR DRDDRR.
Input format:
The first line contains an integer 'N', which denotes the dimensions of the square matrix (maze).

Then 'N' lines follow. Each line contains 'N' space-separated integers denoting the values which would either be 0 denoting a blocked path or 1 denoting the available path in the maze, respectively.
Output format:
For the given maze, print the vector/list of strings representing all the possible paths that the rat can take to reach from source to destination in the maze in sorted order.

Output for each test case will be printed in a separate line.
Note:
You do not need to print anything. It has already been taken care of. Just implement the given function.
Constraints:
2 <= N <= 5
0 <= MATRIX[i][j] <= 1

Where N is the size of the square matrix.

Time Limit: 1sec
Sample Input 1:
4
1 0 0 0 
1 1 0 1
1 1 0 0
0 1 1 1
Sample Output 1:
DDRDRR DRDDRR
Explanation For Sample Input 1:
The rat can reach the destination at (3, 3) from (0, 0) by two paths, i.e. DRDDRR and DDRDRR when printed in sorted order, we get DDRDRR DRDDRR.
Sample Input 2:
2
1 0
1 0
Sample Output 2:
[]
Explanation For Sample Input 2:
As no valid path exists in Sample input 2 so we return an empty list.
"""
from os import *
from sys import *
from collections import *
from math import *


def searchMazeUtil(i, j, arr, n, visited, path, result):
    if i == n - 1 and j == n - 1:
        result.append("".join(path))
        return
    directions = ["D", "U", "L", "R"]
    moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for k in range(4):
        newI, newJ = i + moves[k][0], j + moves[k][1]
        if (
            0 <= newI < n
            and 0 <= newJ < n
            and arr[newI][newJ] == 1
            and not visited[newI][newJ]
        ):
            visited[newI][newJ] = True
            path.append(directions[k])
            searchMazeUtil(newI, newJ, arr, n, visited, path, result)
            path.pop()
            visited[newI][newJ] = False


def searchMaze(arr, n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    path = []
    result = []
    searchMazeUtil(0, 0, arr, n, visited, path, result)
    return result


matrix = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
print(searchMaze(matrix, len(matrix)))
