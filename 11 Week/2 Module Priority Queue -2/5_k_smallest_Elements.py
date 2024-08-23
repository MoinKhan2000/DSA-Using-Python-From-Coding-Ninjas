import heapq


def kSmallest(arr, k):
    output = arr[:k]
    heapq._heapify_max(output)
    print(output)
    for el in arr[k:]:
        if el < output[0]:
            heapq._heapreplace_max(output, el)
            heapq._heapify_max(output)
    return list(reversed(output))


arr = [10, 5, 7, 2, 3, 5, 8, 0, 9,1,1]
k = 4
elements = kSmallest(arr, k)
print(elements)
