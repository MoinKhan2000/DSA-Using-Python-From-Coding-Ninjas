def iterativeFibDp(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    if n <= 2:
        return dp[n]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# TC - O(N) SC- O(1)
def iterativeFibonacci(n):
    a = 0
    b = 1
    c = 0
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
        print(c,end=" ")
    print()
    return c


n = int(input())
print(iterativeFibDp(n))
print(iterativeFibonacci(n))
