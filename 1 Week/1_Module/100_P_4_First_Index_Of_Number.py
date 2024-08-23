def lastIndexFunc(arr, x):
    lastIndex=-1
    # Please add your code here
    for i in range(len(arr)):
        if arr[i]==x:
           lastIndex=i;
    return lastIndex;
    # pass
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndexFunc(arr, x))
