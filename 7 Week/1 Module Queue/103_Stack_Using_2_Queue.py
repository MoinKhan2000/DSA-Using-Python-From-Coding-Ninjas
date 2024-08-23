from sys import stdin


class StackUsing2Queue:
    # Define data members and __init__()

    """----------------- Public Functions of StackUsing2Queue -----------------"""

    def __init__(self):
        # Initialize the stack
        self.q1 = []
        self.q2 = []
        self.q1Front = 0
        self.count = 0

    def getSize(self):
        return self.count

    # Implement the getSize() function

    def isEmpty(self):
        return self.count == 0

    # Implement the isEmpty() function

    def push(self, data):
        self.q1.append(data)
        self.count += 1

    def pop(self):
        if self.isEmpty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        data = self.q1.pop(0)
        self.count -= 1
        self.q1, self.q2 = self.q2, self.q1
        return data

    def top(self):
        if self.isEmpty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        data = self.q1[0]
        self.q2.append(data)
        self.q1, self.q2 = self.q2, self.q1
        return data


# main
q = int(stdin.readline().strip())

stack = StackUsing2Queue()

while q > 0:
    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
