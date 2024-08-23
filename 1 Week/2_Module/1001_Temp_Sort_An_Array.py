""" Aditya Verma YT """


def insertIntoArray(arr, n):
    if len(arr) == 0 or arr[len(arr) - 1] <= n:
        arr.append(n)
        return
    lastElem = arr.pop()
    insertIntoArray(arr, n)
    arr.append(lastElem)


def sortAnArray(arr):
    if len(arr) <= 1:
        return
    lastElem = arr.pop()
    sortAnArray(arr)
    insertIntoArray(arr, lastElem)
    return arr


arr = [15, 41251, 311, 423, 5123, 2]
print(sortAnArray(arr))
# sortAnArray(arr)

# print(arr)
