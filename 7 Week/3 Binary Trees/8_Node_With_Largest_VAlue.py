class BTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printBTree(root):
    if root:
        print(root.data, end=" ")
        printBTree(root.left)
        printBTree(root.right)


def nodeWithLargestValue(root):
    if not root:
        return -1
    elif root:
        return max(
            root.data,
            nodeWithLargestValue(root.left),
            nodeWithLargestValue(root.right),
        )


def inputBTree():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BTree(rootData)
    root.left = inputBTree()
    root.right = inputBTree()
    return root


root = inputBTree()
print(nodeWithLargestValue(root))


""" 
50
10
50
312
-1
-1
35
-1
-1
5
45
-1
-1
55
-1
-1
30
15
65
-1
-1
-1
25
-1
-1
"""
# 312
