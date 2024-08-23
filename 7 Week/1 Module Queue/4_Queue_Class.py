# Built In Queue
import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

# printing all the functinos of Queue()
print("Functions available in Queue():")  # print function name and description for better understanding purpose only!
print("All functions in Queue(): ", dir(q))

while not q.empty():  # 1 2 3 4 5
    print("dequeued item is ", end="")
    print(q.get())


# Built IN Stack
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)


while not q.empty():  # 5 4 3 2 1
    print("dequeued item is ", end="")
    print(q.get())
