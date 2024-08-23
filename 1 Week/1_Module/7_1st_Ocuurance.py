"""
# My Own Logic
def firstIndex(lst, num, index):
    lenOfList = len(lst)
    if index < lenOfList:
        if lst[index] == num:
            return index
        else:
            return firstIndex(lst, num, index + 1)
    else:
        return -1


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
x = int(input())
print(firstIndex(arr, x, 0))
"""

"""
# Sir Logic 1
def firstIndex(a, x):
    l = len(a)
    if l == 0:
        return -1
    if a[0] == x:
        return 0

    smallerList = a[1:]
    smallerListOutput = firstIndex(smallerList, x)

    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1


l = [1, 2, 2, 1, 1, 2, 11, 2, 1, 12, 1]
print(firstIndex(l, 11))
"""


def firstIndex(lst, num, index):
    lenOfList = len(lst)
    if index == lenOfList:
        return -1
    if lst[index] == num:
        return index
    return firstIndex(lst, num, index + 1)

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
x = int(input())
print(firstIndex(arr, x, 0))
 