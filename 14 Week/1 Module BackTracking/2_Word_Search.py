from typing import List


def isValid(row, col, board, visited, word, k, n, m):
    if (
        row < 0
        or row >= n
        or col < 0
        or col >= m
        or visited[row][col]
        or board[row][col] != word[k]
    ):
        return False
    return True


def findWord(row, col, board, visited, word, k, n, m):
    if k == len(word):
        return True

    # dpath = ["D", "L", "R", "U"]
    drow = [1, 0, 0, -1]
    dcol = [0, -1, 1, 0]

    for i in range(4):
        nextRow = row + drow[i]
        nextCol = col + dcol[i]
        if isValid(nextRow, nextCol, board, visited, word, k, n, m):
            visited[nextRow][nextCol] = True
            if findWord(nextRow, nextCol, board, visited, word, k + 1, n, m):
                return True
            visited[nextRow][nextCol] = False
    return False


def present(board: List[List[str]], word: str, n: int, m: int) -> bool:
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                # Making a visited array of size mXn
                visited = [[False for _ in range(m)] for _ in range(n)]
                visited[i][j] = True
                if findWord(i, j, board, visited, word, 1, n, m):
                    # pruning return true if any of the cond is true
                    return True
                # Backtracking
                visited[i][j] = False

    return False


# Test case
board = [
    ["N", "I", "J", "A"],
    ["S", "K", "T", "E"],
    ["M", "O", "P", "Y"],
    ["B", "Q", "G", "H"],
]
print("Matrix: ", board)
print(present(board, "NIJA", len(board), len(board[0])))  # Output should be True
