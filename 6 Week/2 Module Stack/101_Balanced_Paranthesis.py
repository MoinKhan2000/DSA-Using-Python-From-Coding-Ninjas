from sys import stdin


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

    def showStack(self):
        print(self.__data)


def isBalanced(expression):
    stack = Stack()
    # Your code goes here
    for el in expression:
        if (stack.isEmpty() and el == ")") or (stack.isEmpty() and el == "}"):
            return False
        if el == "(" or el == "{":
            stack.push(el)
        if el == ")" and stack.top() == "(" or el == "}" and stack.top() == "{":
            stack.pop()
    return stack.isEmpty()

# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")
