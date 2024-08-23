import sys
def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = 0
    i = 1
    j = len(arr) - 1
    while j >= i:
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        while j >= i and arr[j] >= arr[pivot]:
            j -= 1
        if j >= i:
            arr[i], arr[j] = arr[j], arr[i]
        # print(arr)
    arr[pivot], arr[j] = arr[j], arr[pivot]

    left = QuickSort(arr[:j])
    right = QuickSort(arr[j + 1 :])
    return left + [arr[j]] + right


numberOfTimes = int(input(""))
for k in range(numberOfTimes):
    num = int(input())
    if num > 0:
        l = [int(x) for x in input().split()]
        sortedList = QuickSort(l)
        for el in sortedList:
            print(el, end=" ")
        print()

sys.exit()