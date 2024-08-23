from sys import stdin

""" 
1 4 9 3 2   #leftSum=0 sum=sum(arr)
sum-=arr[i]
if leftSum==sum:
    return i 
else: 
    leftSum+=arr[i];
"""


def arrayEquilibriumIndex(arr, n):
    sumOfArray = sum(arr)
    leftSum = 0
    for i in range(0, n):
        sumOfArray -= arr[i]
        if leftSum == sumOfArray:
            return i
        else:
            leftSum += arr[i]
    return -1


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1
