"""  
Code : Max Priority Queue
Send Feedback
Implement the class for Max Priority Queue which includes following functions -


1. getSize -
Return the size of priority queue i.e. number of elements present in the priority queue.


2. isEmpty -
Check if priority queue is empty or not. Return true or false accordingly.


3. insert -
Given an element, insert that element in the priority queue at the correct position.


4. getMax -
Return the maximum element present in the priority queue without deleting. Return -Infinity if priority queue is empty.


5. removeMax -
Delete and return the maximum element present in the priority queue. Return -Infinity if priority queue is empty.


Note : main function is given for your reference which we are using internally to test the class.

"""


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

    def getMax(self):
        if not self.isEmpty():
            max_node = self.pq[0].value
            return max_node
        return None

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = (
                    self.pq[childIndex],
                    self.pq[parentIndex],
                )
                childIndex = parentIndex
            else:
                break

    def __percolateDown(self):
        parentIndex = 0
        while True:
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2
            maxElemIndex = parentIndex
            if (
                leftChildIndex < self.getSize()
                and self.pq[leftChildIndex].priority > self.pq[maxElemIndex].priority
            ):
                maxElemIndex = leftChildIndex
            if (
                rightChildIndex < self.getSize()
                and self.pq[rightChildIndex].priority > self.pq[maxElemIndex].priority
            ):
                maxElemIndex = rightChildIndex
            if parentIndex != maxElemIndex:
                self.pq[parentIndex], self.pq[maxElemIndex] = (
                    self.pq[maxElemIndex],
                    self.pq[parentIndex],
                )
                parentIndex = maxElemIndex
            else:
                break

    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def removeMax(self):
        """Removeing the maximum element from the max heap"""
        if self.isEmpty():
            return None
        else:
            self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
            maxElem = self.pq.pop()
            self.__percolateDown()
            return maxElem.value


myPq = PriorityQueue()
# curr_input = [int(ele) for ele in input().split()]
# choice = curr_input[0]
# i = 1
# while choice != -1:
#     if choice == 1:
#         element = curr_input[i]
#         i += 1
#         myPq.insert(element, element)
#     elif choice == 2:
#         print(myPq.getMax())
#     elif choice == 3:
#         print(myPq.removeMax())
#     elif choice == 4:
#         print(myPq.getSize())
#     elif choice == 5:
#         if myPq.isEmpty():
#             print("true")
#         else:
#             print("false")
#         break
#     else:
#         pass
#     choice = curr_input[i]
#     i += 1
# myPq.insert('A',100)
# myPq.insert('B',99)
# myPq.insert('C',99)
# myPq.insert('D',97)
# myPq.insert('E',96)
# for i in range(5):
#     print(myPq.removeMax())


arr = [1, 3, 54, 562, 2, 3]
for el in arr:
    myPq.insert(el, el)
for i in range(len(arr)):
    print(myPq.removeMax(), end=" ")


# 54 562 3 3 2 1  it should print in sorted manner but wrong
