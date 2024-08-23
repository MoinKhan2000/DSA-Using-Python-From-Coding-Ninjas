from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


# Time complexity is about O(n2) to O(nLog n)
def isBalanced(root):
    if root == None:
        return True
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    if (max(leftHeight, rightHeight) - min(leftHeight, rightHeight)) > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)

    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False


def getHeightAndCheckBalancedAdvance(root):
    if root is None:
        return 0, True
    lh, isLeftBalanced = getHeightAndCheckBalancedAdvance(root.left)
    rh, isRightBalanced = getHeightAndCheckBalancedAdvance(root.right)
    h = 1 + max(lh, rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False


def inputBTree():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    root.left = inputBTree()
    root.right = inputBTree()
    return root


def printLevelWise(root):
    if root == None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=" ")
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ


root = inputBTree()
# print(isBalanced(root))
print(getHeightAndCheckBalancedAdvance(root))
# isBalanced(root)
