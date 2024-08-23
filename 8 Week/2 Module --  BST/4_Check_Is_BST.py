import queue
import math


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(arr):
    if not arr:
        return None
    mid = math.floor(len(arr) / 2)
    root = BinaryTreeNode(arr[mid])
    root.right = constructBST(arr[:mid])
    root.left = constructBST(arr[mid + 1 :])
    return root


def preOrder(root):
    if root == None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


def minTree(root):
    if root is None:
        return float("inf")
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)


def maxTree(root):
    if root is None:
        return float("-inf")
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)


def checkIsBST(root):
    if root is None or (root.left is None and root.right is None):
        return True
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)

    if root.data > rightMin or root.data <= leftMax:
        return False
    return checkIsBST(root.left) and checkIsBST(root.right)


# Main
n = int(input())
if n > 0:
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst[::-1])
preOrder(root)
print()
print(checkIsBST(root))