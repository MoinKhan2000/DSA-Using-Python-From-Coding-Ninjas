from typing import List


def isItSudoku(board):
    res = set()
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element > 0:
                if (
                    (i, element) in res
                    or (element, j) in res
                    or (i // 3, j // 3, element) in res
                ):
                    return False
                res.add((i, element))
                res.add((element, j))
                res.add((i // 3, j // 3, element))
    return True


matrix = [
    [9, 0, 0, 0, 2, 0, 7, 5, 0],
    [6, 0, 0, 0, 5, 0, 0, 4, 0],
    [0, 2, 0, 4, 0, 0, 0, 1, 0],
    [2, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 5, 0, 9, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 1],
    [0, 1, 0, 0, 0, 5, 0, 8, 0],
    [0, 9, 0, 0, 7, 0, 0, 0, 4],
    [0, 8, 2, 0, 4, 0, 0, 0, 6],
]

seen = set()
print(isItSudoku(matrix))  # Output: False
print(seen)
