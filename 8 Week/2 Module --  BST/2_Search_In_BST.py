""" 
The time complexity of operations in a Binary Search Tree (BST) depends on the balance of the tree. There are two main cases to consider:

Balanced BST:

Searching for an element: O(log N) on average, where N is the number of nodes in the tree. In a balanced tree, you can eliminate half of the remaining nodes in each step, resulting in a logarithmic time complexity.
Insertion of an element: O(log N) on average. The insertion process is similar to searching, where you navigate the tree to find the correct location for the new node.
Deletion of an element: O(log N) on average. Similar to insertion and searching, the deletion process involves navigating the tree.

      10
     /  \
    5   15
   / \    \
  3   7   20


Unbalanced BST (worst case):

In the worst case, when the BST is completely unbalanced (essentially a linked list), all operations (search, insert, delete) have a time complexity of O(N), where N is the number of nodes in the tree. This worst-case scenario can occur when elements are inserted in sorted or ascending/descending order.
Efforts are made to keep BSTs balanced in practice. Self-balancing binary search trees, such as AVL trees and Red-Black trees, are designed to automatically maintain balance during insertions and deletions, ensuring that the worst-case time complexity remains O(log N).

In summary, the time complexity of BST operations is O(log N) on average for a balanced tree, but it can degrade to O(N) in the worst case for an unbalanced tree. Self-balancing BSTs help mitigate this issue and guarantee logarithmic time complexity.

1
 \
   3
    \
     6
      \
        7
"""

import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printBTreeAdvance(root):
    if root is None:
        return
    if root:
        print(str(root.data), end=" : ")
        if root.left:
            print("Left :", root.left.data, ", ", end="")
        if root.right:   
            print("Right :", root.right.data)
        else:
            print()
        printBTreeAdvance(root.left)
        printBTreeAdvance(root.right)


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


def searchNodeInBST(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    elif root.data > x:
        #         print("searching in left")
        return searchNodeInBST(root.left, x)
    else:
        return searchNodeInBST(root.right, x)


n = int(input("Enter the element to search in BST\n"))
printBTreeAdvance(root)
print(searchNodeInBST(root, n))
