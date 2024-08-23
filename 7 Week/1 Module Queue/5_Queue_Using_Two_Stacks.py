from os import *
from sys import *
from collections import *
from math import *


class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        # Write your code here
        self.stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """

    def dequeue(self):
        if len(self.stk1) == 0:
            return -1
        while len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())
        data = self.stk1.pop()
        while len(self.stk2) > 0:
            self.stk1.append(self.stk2.pop())
        return data

    def frontPointer(self):
        if len(self.stk1) == 0:
            return -1
        # return self.stk1[0]

        while len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())
        data = self.stk1.pop()
        self.stk2.append(data)
        while len(self.stk2) > 0:
            self.stk1.append(self.stk2.pop())
        return data

    def size(self):
        return len(self.stk1)

    def isEmpty(self):
        return len(self.stk1) == 0


# main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0:
    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        print(queue.enqueue(data))

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
