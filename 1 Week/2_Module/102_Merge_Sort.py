def mergeArray(arr1, arr2):
    i = 0
    j = 0
    arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j]) 
            j += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr


def mergeSortRecursively(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftArr, rightArr = arr[:mid], arr[mid:]

    leftArr = mergeSortRecursively(leftArr)
    rightArr = mergeSortRecursively(rightArr)

    sortedArray = mergeArray(leftArr, rightArr)
    return sortedArray


num = int(input())
while num > 0:
    l = [int(x) for x in input().split()]
    sortedList = mergeSortRecursively(l)
    for el in sortedList:
        print(el, end=" ")
    print('')
    num-=1
