def checkNumber(arr, x):
    # Please add your code here
    for i in range(len(arr)):
        if arr[i]==x:
            return True
    return False
    # pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')