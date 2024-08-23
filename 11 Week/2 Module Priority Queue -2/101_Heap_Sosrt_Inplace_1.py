""" 
Inplace Heap Sort
Send Feedback
Given an integer array of size N. Sort this array (in decreasing order) using heap sort.
Note: Space complexity should be O(1).
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array or N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output Format :
The first and only line of output contains array elements after sorting. The elements of the array in the output are separated by single space.
Constraints :
1 <= n <= 10^6
Time Limit: 1 sec
Sample Input 1:
6 
2 6 8 5 4 3
Sample Output 1:
8 6 5 4 3 2
"""


def upheapify(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break


def downHeapify(arr, n, i):
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[largest]:
            largest = left
        if right < n and arr[right] < arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break


def heapSort(arr):
    n = len(arr)
    # Making inplace min heap
    for i in range(1, n):
        upheapify(arr, i)
    print("inplace heap ", arr)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        downHeapify(arr, i, 0)


arr = [2, 235, 35, 23, 6, 3, 4, 23, 62, 2, 3]
arr = [10, 5, 8, 1, 4]
arr = [10, 5, 11, 2, 3, 7, 12, 1, 6]
heapSort(arr)
print("Sorted array is:", arr)
