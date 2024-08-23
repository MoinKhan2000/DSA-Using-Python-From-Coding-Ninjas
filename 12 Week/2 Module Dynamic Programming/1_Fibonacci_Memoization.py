import time


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        left = fib(n - 1)
        right = fib(n - 2)
        return left + right


def fibDP(n):
    if n == 0 or n == 1:
        return n
    elif memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fibDP(n - 1) + fibDP(n - 2)
        return memo[n]


# Memoization table
n = int(input("Enter a number: "))
# Enter a number: 32
memo = [-1] * (n + 1)

# Measure time for fib() without DP
start_time = time.time()
result1 = fib(n)
end_time = time.time()
print(f"Without DP: {result1}, Time taken: {end_time - start_time:.6f} seconds")
# Without DP: 2178309, Time taken: 0.904584 seconds


# Measure time for fibDP() with DP
start_time = time.time()
result2 = fibDP(n)
end_time = time.time()
print(f"With DP: {result2}, Time taken: {end_time - start_time:.6f} seconds")
# With DP: 2178309, Time taken: 0.000000 seconds

print(memo)