import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    print(root.data, end="")
    print(":L:", end="")
    print(root.left.data, end="") if root.left else print(-1, end="")
    print(",R:", end="")
    print(root.right.data) if root.right else print(-1)
    q = queue.Queue()
    q.put(root.left)
    q.put(root.right)
    while not q.empty():
        node = q.get()
        if not node:
            continue
        print(node.data, end="")
        print(":L:", end="")
        print(node.left.data, end="") if node.left else print(-1, end="")
        print(",R:", end="")
        print(node.right.data) if node.right else print(-1)
        q.put(node.left) if node.left else None
        q.put(node.right) if node.right else None


def takeInputLevelWise():
    q = queue.Queue()
    print("Enter root")

    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print("Enter left child of ", currentNode.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)
        print("Enter right  child of ", currentNode.data)

        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)
    return root


root = takeInputLevelWise()
printLevelWise(root)
