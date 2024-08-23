def isValidMove(row, col, arr, visited, n):
    if (
        row < 0
        or row >= n
        or col < 0
        or col >= n
        or visited[row][col]
        or arr[row][col] == 0
    ):
        return False
    return True


def explore(row, col, arr, visited, n, path, ans):
    if arr[row][col] == 0:
        return
    if row == n - 1 and col == n - 1:
        ans.append("".join(path))
        return
    drow = [1, 0, 0, -1]
    dcol = [0, -1, 1, 0]
    dpath = ["D", "L", "R", "U"]

    # (row + drow[i] , col + col[i] ) dpath[i]

    for i in range(4):
        nextRow = row + drow[i]
        nextCol = col + dcol[i]
        if isValidMove(nextRow, nextCol, arr, visited, n):
            visited[nextRow][nextCol] = True
            path.append(dpath[i])
            explore(nextRow, nextCol, arr, visited, n, path, ans)
            visited[nextRow][nextCol] = False
            path.pop()

    return ans


def main():
    matrix = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # matrix = [
    #     [1, 0, 0, 0],
    #     [1, 1, 0, 0],
    #     [1, 1, 0, 0],
    #     [0, 1, 1, 1],
    # ]
    n = len(matrix)
    visited = [[False for _ in range(n)] for _ in range(n)]
    path = []
    ans = []
    explore(0, 0, matrix, visited, n, path, ans)
    return ans


print(main())
