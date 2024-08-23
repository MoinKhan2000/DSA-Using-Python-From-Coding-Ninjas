class Stack:
    def __init__(self):
        # Declaring data as a private variable
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Hey! Stack Is Empty!!")
            return -1
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Hey! Stack Is Empty!!")
            return -1
        return self.__data[len(self.__data) - 1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return True if len(self.__data) == 0 else False


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
# print(s.pop())
# print(s.top())

while s.isEmpty() is False:
    print("Poping out ", end="")
    print(s.pop())

print(s.top())
