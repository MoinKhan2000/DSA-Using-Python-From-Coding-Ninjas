def downHeapify(arr, i, n):
    parentIndex = i
    leftChildIndex = 2 * parentIndex + 1
    rightChildIndex = 2 * parentIndex + 2
    while leftChildIndex < n:
        minIndex = parentIndex
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
        elif rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex
        if minIndex == parentIndex:
            return
        else:
            arr[parentIndex], arr[minIndex] = arr[minIndex], arr[parentIndex]
            parentIndex = minIndex
            leftChildIndex = parentIndex * 2 + 1
            rightChildIndex = parentIndex * 2 + 2


def heapSort(arr, n):
    # Build The Heap O(N)
    for i in range(n // 2, -1, -1):
        downHeapify(arr, i, n)

    # Removing n elements from the heap and put them at correct position
    for i in range(n - 1, 0, -1):
        # Putting the minimum element i at n-1
        arr[i], arr[0] = arr[0], arr[i]
        downHeapify(arr, 0, i)
    return


arr = [int(x) for x in input().split()]
heapSort(arr, len(arr))
print(arr)
