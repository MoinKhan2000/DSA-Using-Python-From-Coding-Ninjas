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
        lastvaluement = self.pq.pop()
        if self.getSize() != 0:
            self.pq[0] = lastvaluement
            self.__percolateDown()
            return minValue
        else:
            return minValue

    def removeMin2(self):
        if self.isEmpty() is True:
            return None
        minValue = self.pq[0].value
        minValue = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__percolateDown()
        return minValue


myPq = PriorityQueue()


arr = [1, 3, 54, 562, 2, 3]
for el in arr:
    myPq.insert(el, el)
for i in range(len(arr)):
    print(myPq.removeMin(), end=" ")

# 562 54 3 3 2 1


# myPq.insert("A", 10)
# myPq.insert("C", 5)
# myPq.insert("B", 19)
# myPq.insert("D", 4)
# for i in range(4):
#     print(myPq.removeMin())
#     print("-------------------------")
