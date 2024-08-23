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


# def checkBSTAdvance(root, min_val=float("-inf"), max_val=float("inf")):
#     if root is None: 
#         return True, float("inf"), float("-inf")

#     if root.data < min_val or root.data > max_val:
#         return False, float("inf"), float("-inf")

#     isLeftBST, min_left, max_left = checkBSTAdvance(root.left, min_val, root.data)
#     isRightBST, min_right, max_right = checkBSTAdvance(
#         root.right, root.data, max_val
#     )

#     if isLeftBST and isRightBST:
#         return True, min_left, max_right
#     else:
#         return False, float("inf"), float("-inf")


def checkBSTAdvance(root,minRange=float('-inf'), maxRange=float('inf')):
    if root is None:
        return True
    if root.data <= minRange or root.data >maxRange:
        return False
    isLeftWithinConstraints = checkBSTAdvance(root.left,minRange, root.data -1)
    isRightWithinConstaints = checkBSTAdvance(root.right, root.data, maxRange)
    if isLeftWithinConstraints and isRightWithinConstaints:
        return True
    return False

n = int(input())
if n > 0:
    # Give the input as a sorted array
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst[::-1])
preOrder(root)
print()
print(checkBSTAdvance(root))
