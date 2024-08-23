def isSafe(row, col, configuration, n):
    # Same diagonal
    for i in range(row):
        for j in range(n):
            if configuration[i][j] == 1:
                if row == i:
                    return False
                if col == j:
                    return False
                if row - col == i - j:
                    return False
                if row + col == i + j:
                    return False
    return True


def solve(row, configuraion, n, ans):
    if row >= n:
        tempAns = []
        for i in range(n):
            for j in range(n):
                tempAns.append(configuraion[i][j])
        ans.append(tempAns)
        return
    for i in range(n):
        if isSafe(row, i, configuraion, n):
            configuraion[row][i] = 1
            solve(row + 1, configuraion, n, ans)
            # backtrack
            configuraion[row][i] = 0


def solveNQueens(n):
    ans = []
    configuration = [[0 for _ in range(n)] for _ in range(n)]
    solve(0, configuration, n, ans)
    totLen = len(ans[0])
    j = 0
    for el in ans:
        for li in el:
            print(li, end=" ")
            j += 1
            if j == totLen // 2:
                print()
        j = 0
        print()
    return ans


(solveNQueens(4))
