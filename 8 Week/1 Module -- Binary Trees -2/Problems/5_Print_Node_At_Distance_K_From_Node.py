""" 
Print nodes at distance k from node
Send Feedback
You are given a Binary Tree of type integer, a integer value of target node's data, and an integer value K.
Print the data of all nodes that have a distance K from the target node. The order in which they would be printed will not matter.
Example:
For a given input tree(refer to the image below):
1. Target Node: 5
2. K = 2
alt txt

Starting from the target node 5, the nodes at distance K are 7 4 and 1.
Input Format:
The first line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

The second line of input contains two integers separated by a single space, representing the value of the target node and K, respectively.
Output Format:
All the node data at distance K from the target node will be printed on a new line.

The order in which the data is printed doesn't matter.
Constraints:
1 <= N <= 10^5
Where N is the total number of nodes in the binary tree.
1 ≤ data of node ≤ 10^9
1 ≤ target ≤ 10^9

Time Limit: 1 sec
Sample Input 1:
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
3 1
Sample Output 1:
9
6
Sample Input 2:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
3 3
Sample Output 2:
4
5
"""

from sys import stdin, setrecursionlimit
import queue
from typing import List

setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findPath(root, x, path):
    if root is None:
        return False
    path.append(root.data)
    if root.data == x:
        return True
    if (root.left and findPath(root.left, x, path)) or (
        root.right and findPath(root.right, x, path)
    ):
        return True

    path.pop()
    return False


def pathInATree(root: BinaryTreeNode, x: int) -> List[int]:
    path = []
    if findPath(root, x, path):
        return path
    else:
        return []


def printNodesAtKDistance(root, k, block):
    if root is None or root == block:
        return
    if k == 0:
        print(root.data)
        return
    printNodesAtKDistance(root.left, k - 1, block)
    printNodesAtKDistance(root.right, k - 1, block)
    return


def findPath(root, data, arr=[]):
    if root is None:
        return []
    if root.data == data:
        arr.append(root)
        return arr
    if findPath(root.left, data, arr) or findPath(root.right, data, arr):
        arr.append(root)
        return arr
    return []


def nodesAtDistanceK(root, node, k):
    # Your code goes here
    if root is None:
        return
    path = pathInATree(root, node)
    for i in range(len(path)):
        printNodesAtKDistance(path[i], k - i, None if i == 0 else path[i - 1])


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root is None:
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


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)
