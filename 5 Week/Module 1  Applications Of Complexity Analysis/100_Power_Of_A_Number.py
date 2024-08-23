def power(n, x):
    if x == 0:
        return 1
    elif x == 1:
        return n
    if x % 2 == 0:
        halfRes = power(n, x / 2)
        return halfRes * halfRes
    else:
        halfRes = power(n, x // 2)
        return halfRes * halfRes * n


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n, x = list(int(i) for i in input().strip().split(" "))
print(power(n, x))
