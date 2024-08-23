def fibonacchiRecursive(n):
    if n == 1 or n == 2:
        return 1
    return fibonacchiRecursive(n - 1) + fibonacchiRecursive(n - 2)


print(fibonacchiRecursive(6))
