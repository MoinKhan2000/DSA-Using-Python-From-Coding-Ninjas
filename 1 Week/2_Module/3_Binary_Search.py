"""
# My Logic
def binarySearch(arr, n, start, end):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            return binarySearch(arr, n, start, mid - 1)
        else:
            return binarySearch(arr, n, mid + 1, end)
    else:
        return -1


arr = [1, 2, 3, 43, 54, 55, 76, 98, 123, 124, 234]
n = 54
print(binarySearch(arr, n, 0, len(arr) - 1))
"""


def binarySearch(a, n, s, e):
    if s >= e:
        return -1
    mid = (s + e) // 2
    if a[mid] == n:
        return mid
    elif a[mid] > n:
        return binarySearch(a, n, s, mid - 1)
    else:
        return binarySearch(a, n, (mid + 1), e)


arr = [1, 2, 3, 34, 46, 54, 56, 76, 78, 98, 122]
print(binarySearch(arr, 34, 0, len(arr) - 1))
