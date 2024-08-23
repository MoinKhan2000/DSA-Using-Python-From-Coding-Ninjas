"""
BST Class
Send Feedback
Implement the BST class which includes following functions -
1. insert -
Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node, insert it in the left subtree.
2. search
Given an element, find if that is present in BST or not. Return true or false.
3. delete -
Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.
4. printTree (recursive) -
Print the BST in in the following format -
For printing a node with data N, you need to follow the exact format -
N:L:x,R:y
where, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
There is no space in between.
You need to print all nodes in the recursive format in different lines.
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTree(self):
        def printTreeHelper(root):
            if root is None:
                return
            print(root.data, end=":")
            if root.left:
                print("L:" + str(root.left.data), end=",")
            if root.right:
                print("R:" + str(root.right.data), end="")
            print()
            printTreeHelper(root.left)
            printTreeHelper(root.right)

        printTreeHelper(self.root)

    def search(self, data):
        def isPresentHelper(root, data):
            if root is None:
                return False
            if root.data == data:
                return True
            if root.data > data:
                return isPresentHelper(root.left, data)
            else:
                return isPresentHelper(root.right, data)

        return isPresentHelper(self.root, data)

    def insert(self, data):
        self.numNodes += 1

        def insertNodeHelper(root, data):
            if root is None:  
                node = BinaryTreeNode(data)
                return node
            if root.data >= data:
                root.left = insertNodeHelper(root.left, data)
            else:
                root.right = insertNodeHelper(root.right, data)
            return root

        self.root = insertNodeHelper(self.root, data)

    def delete(self, data):
        def findMinValueNode(root):
            while root.left is not None:
                root = root.left
            return root.data

        def deleteDataHelper(root, data):
            if root is None:
                return False, None
            if root.data < data:
                deleted, root.right = deleteDataHelper(root.right, data)
            elif root.data > data:
                deleted, root.left = deleteDataHelper(root.left, data)
            else:
                if root.right is None and root.left is None:
                    return True, None
                elif root.right is None:
                    return True, root.left
                elif root.left is None:
                    return True, root.right
                else:
                    minVal = findMinValueNode(root.right)
                    root.data = minVal
                    deleted, root.right = deleteDataHelper(root.right, minVal)
                    return True, root
            return deleted, root

        deleted, self.root = deleteDataHelper(self.root, data)
        if deleted:
            self.numNodes -= 1

    def count(self):
        return self.numNodes

b = BST()
q = int(input())
while q > 0:
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q -= 1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
