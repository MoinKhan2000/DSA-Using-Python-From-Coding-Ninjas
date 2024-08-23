class Node:
    def __init__(self, data):
        # data is the value of node
        # next points to the next node in linked list
        self.data = data
        self.next = None


a = Node(12)
b = Node(5)
a.next = b

print(a.data, a.next.data)
