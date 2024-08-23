def powerIterative(n, x):
    i = 0
    anx = 1
    while i < x:
        anx *= n
        i += 1

    print(anx)


# Time Complexity : O(n)
# Space Complexity : O(1)


def powerRecursive(n, x):
    if x == 0:
        return 1
    elif x == 1:
        return n
    return n * powerRecursive(n, x - 1)


def betterPowerRecursive(n, x):
    if x == 0:
        return 1
    elif x == 1:
        return n
    if x % 2 == 0:
        halfRes = betterPowerRecursive(n, x / 2)
        return halfRes * halfRes
    else:
        halfRes = betterPowerRecursive(n, x // 2)
        return halfRes * halfRes * n


# Time Complexity : O(n)
# Space Complexity : O(n)


powerIterative(2, 9)
print(powerRecursive(2, 9))
print(betterPowerRecursive(2, 9))
