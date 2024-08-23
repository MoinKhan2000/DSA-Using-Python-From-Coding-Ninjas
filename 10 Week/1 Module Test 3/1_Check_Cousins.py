"""

Check cousins
Send Feedback
Given the binary Tree and two nodes say ‘p’ and ‘q’. Determine whether the two nodes are cousins of each other or not. Two nodes are said to be cousins of each other if they are at same level of the Binary Tree and have different parents.
Do it in O(n).
Input format :
Line 1 : Nodes in level order form (separated by space). If any node does not have left or right child, take -1 in its place
Line 2 : integer value of p 
Line 3 : Integer value of q
Output format :
true or false
Constraints :
1 <= N <= 10^5
Sample Input :
5 6 10 2 3 4 -1 -1 -1 -1 9 -1 -1 -1 -1
2
4
Sample Output :
true


"""
import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findHeightParent(root, data, height):
    if root is None:
        return None, 0
    if (root.left and root.left.data == data) or (root.right and root.right.data == data):
        return root, height
    left_parent, left_height = findHeightParent(root.left, data, height + 1)
    right_parent, right_height = findHeightParent(root.right, data, height + 1)

    if left_parent:
        return left_parent, left_height
    if right_parent:
        return right_parent, right_height

    return None, 0


def checkCousins(root, p, q):
    if root.data == p or root.data == q:
        return False

    xparent, xHeight = findHeightParent(root, p, 0)
    yparent, yHeight = findHeightParent(root, q, 0)
    print(xparent.data, yparent.data)
    if xparent != yparent and xHeight == yHeight:
        return True

    return False


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root, p, q)
if ans is True:
    print("true")
else:
    print("false")
