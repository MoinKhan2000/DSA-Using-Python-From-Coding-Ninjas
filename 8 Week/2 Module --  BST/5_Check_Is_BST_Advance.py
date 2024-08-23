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


def checkBSTAdvance(root):
    if root is None:
        return True, float("inf"), float("-inf")

    isLeftBST, leftMin, leftMax = checkBSTAdvance(root.left)
    isRightBST, rightMin, rightMax = checkBSTAdvance(root.right)
    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    isBST = True
    if root.data <= leftMax or root.data > rightMin:
        isBST = True
    if not (isLeftBST) or not (isRightBST):
        isBST = False
    return isBST, minimum, maximum


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
