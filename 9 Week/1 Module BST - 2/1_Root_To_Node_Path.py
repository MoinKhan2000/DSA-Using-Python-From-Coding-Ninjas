from sys import stdin
import queue
import math


class treeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rootToNodePath(root, val):
    if root is None:
        return None
    if root.data == val:
        l = list()
        l.append(root.data)
        return l
    leftOutput = rootToNodePath(root.left, val)
    if leftOutput is not None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutput = rootToNodePath(root.right, val)
    if rightOutput is not None:
        rightOutput.append(root.data)
        return rightOutput
    return None


def takeInputLevelWise():
    q = queue.Queue()
    print("Enter root")

    rootData = int(input())
    if rootData == -1:
        return None
    root = treeNode(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print("Enter left child of ", currentNode.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = treeNode(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)
        print("Enter right  child of ", currentNode.data)

        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = treeNode(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)
    return root


root = takeInputLevelWise()
data = int(input())
print(rootToNodePath(root, data))
