from sys import stdin


# Following is the structure of the node class for a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    # Define data members and __init__()
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.count = 0

    """----------------- Public Functions of Stack -----------------"""

    def getSize(self):
        return self.count

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
            self.count += 1
        else:
            self.rear.next = newNode
            self.rear = self.rear.next
            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return -1
        data = self.front.data
        self.front = self.front.next
        self.count -= 1
        return data

    def frontPointer(self):
        return self.front.data if self.front is not None else -1


# main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0:
    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2:
        print(queue.dequeue())

    elif choice == 3:
        print(queue.frontPointer())

    elif choice == 4:
        print(queue.getSize())

    else:
        if queue.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
