class PriorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value

    def __percolateDown(self):
        parentIndex = 0
        while True:
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2
            smallestIndex = parentIndex
            if (
                leftChildIndex < self.getSize()
                and self.pq[leftChildIndex].priority < self.pq[smallestIndex].priority
            ):
                smallestIndex = leftChildIndex
            if (
                rightChildIndex < self.getSize()
                and self.pq[rightChildIndex].priority < self.pq[smallestIndex].priority
            ):
                smallestIndex = rightChildIndex
            if parentIndex != smallestIndex:
                self.pq[smallestIndex], self.pq[parentIndex] = (
                    self.pq[parentIndex],
                    self.pq[smallestIndex],
                )
                parentIndex = smallestIndex
            else:
                break

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2

            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = (
                    self.pq[childIndex],
                    self.pq[parentIndex],
                )
                childIndex = parentIndex
            else:
                break

    def insert(self, value, priority):
        pqNode = PriorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def removeMin(self):
        if self.isEmpty() is True:
            return None
        minValue = self.pq[0].value
        minValue = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__percolateDown()
        return minValue


def heapSort(arr):
    myPq = PriorityQueue()
    for i in arr:
        myPq.insert(i, i)
    arr = []
    for j in range(len(myPq.pq)):
        arr.append(myPq.removeMin())
    return arr


arr = [1, 2, 562, 23, 62, 23, 325, 2, 23, 2]
print(heapSort(arr))
