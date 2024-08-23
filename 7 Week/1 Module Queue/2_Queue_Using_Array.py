class QueueUsingArray:
    def __init__(self) -> None:
        self.items = []
        self.front = 0
        self.count = 0

    def isEmpty(self):
        if (self.count) == 0:
            return True
        return False

    def enqueue(self, data):
        self.items.append(data)
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return -1
        front_item = self.items[self.front]
        self.front += 1
        self.count -= 1
        return front_item

    def front(self):
        if self.isEmpty():
            return None
        return self.items[self.front]

    def Size(self):
        return self.count


q = QueueUsingArray()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)

print("Size of queue is ", q.Size())  # Output : 5
print("Front item in the queue", q.Front())
# Output :- 1 (First element inserted into QUEUE)
print("Dequeued Elemeent ", q.Dequeue())
print("Front item in the queue", q.Front())

while not q.isEmpty():
    print("Popped element ", q.Dequeue())
# print(q.items)
print(q.Dequeue())
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)

print("Size of queue is ", q.Size())  # Output : 5
print(q.Front())
