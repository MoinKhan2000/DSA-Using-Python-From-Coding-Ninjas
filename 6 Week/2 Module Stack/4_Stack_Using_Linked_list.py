class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # Declaring data as a private variable
        self.__head = None
        self.__count = 0

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            print("Hey! Stack is Underflow!!.")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def top(self):
        if self.isEmpty():
            print("Hey! Stack is Underflow!!.")
            return
        data = self.__head.data
        return data

    def size(self):
        return self.__count

    def isEmpty(self):
        return True if self.__head is None else False


s = Stack()
s.push(1)
s.push(123)
s.push(234)
s.push(12)
s.push(33)
s.push(123)
s.push(59)
s.push(234)
s.push(98)
print(s.size())
print(s.top())
