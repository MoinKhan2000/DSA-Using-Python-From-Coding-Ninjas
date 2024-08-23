def arrayEquilibriumIndex(arr, n):
    sumOfArray = sum(arr)
    leftSum = 0
    for i in range(0, n):
        rightSum = sumOfArray - leftSum - arr[i]
        if leftSum == rightSum:
            return i
        leftSum += arr[i]

    return -1


arr = [1, 3, 4, 2, 2, 5, 4, 1]
print(arrayEquilibriumIndex(arr, len(arr)))
