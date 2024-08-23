def sumArray(arr):
    # Please add your code here
    lenOfArr=len(arr)
    sum=0
    if lenOfArr==1:
        return arr[0]
    else:
        return int(arr[0])+int(sumArray(arr[1:]))
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
