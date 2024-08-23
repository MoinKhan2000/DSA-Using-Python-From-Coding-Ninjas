import sys
import math

sys.setrecursionlimit(10**9)


def f(n, dp):
    if n in [0, 1, 2, 3]:
        return n
    if dp[n] != -1:
        return dp[n]

    ans = 1e9 + 7
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        ans = min(ans, 1 + f(n - i * i, dp))

    dp[n] = ans
    return dp[n]


def minStepsTo1Iter(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    ans = 1e9 + 7
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        dp[n] = min(ans, 1 + dp[n - i * i])
    return dp[n]


def minStepsTo1(n):
    # dp = [-1 for _ in range(n + 1)]
    # return f(n, dp)
    print(minStepsTo1Iter(n))


n = int(input())
ans = minStepsTo1(n)
print(ans)
