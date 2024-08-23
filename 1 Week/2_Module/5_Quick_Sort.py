# def partition(arr, start, end):
#     pivot = arr[start]

#     count = 0
#     for i in range(start, end + 1):
#         if arr[i] < pivot:
#             count += 1
#     pivot_index = start + count
#     arr[pivot_index], arr[start] = arr[start], arr[pivot_index]
#     i = start
#     j = end
#     while i < j:
#         if arr[i] < pivot:
#             i += 1
#         elif arr[j] >= pivot:
#             j -= 1
#         else:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#     return pivot_index


# def quickSort(arr, start, end):
#     if start > end:
#         return
#     pivot_index = partition(arr, start, end)
#     quickSort(arr, start, pivot_index - 1)
#     quickSort(arr, pivot_index + 1, end)
#     return arr


# arr = [235, 2323, 523, 2, 35, 23412, 34124, 32]
# # print(quickSort(arr, 0, len(arr) - 1))
# print(partition(arr, 0, len(arr) - 1))
# print(arr)


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = 0
    i = 1
    j = len(arr) - 1
    while j >= i:
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        while j >= i and arr[j] > arr[pivot]:
            j -= 1
        if j >= i:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]

    left = quickSort(arr[:j])
    right = quickSort(arr[j + 1 :])
    return left + [arr[j]] + right


arr = [235, 2323, 523, 2, 35, 23412, 34124, 32]
print(quickSort(arr))
print(arr[::-1])
# print(arr)
# [2, 32, 35, 235, 523, 2323, 23412, 34124]
# [2323, 34124, 23412, 523, 235, 35, 32, 2]