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


def numNodes(root):
    if not root:
        return 0
    else:
        count = 0
        count += 1 + numNodes(root.left) + numNodes(root.right)
        return count


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


def heightOfTree(root, count=0):
    if root is None:
        return 0
    return 1 + max(heightOfTree(root.left), heightOfTree(root.right))


def inputBTree():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BTree(rootData)
    root.left = inputBTree()
    root.right = inputBTree()
    return root


def numberOfLeafNodes(root, count=0):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return None
    count += numberOfLeafNodes(root.left, count)
    count += numberOfLeafNodes(root.right, count)
    return count


def printRootToNodePath(root, data, arr=[]):
    if root is None:
        return []
    if root.data == data:
        arr.append(root.data)
        return arr
    if (printRootToNodePath(root.left, data, arr) or printRootToNodePath(root.right, data, arr)):
        arr.append(root.data)
        return arr
    return []


root = inputBTree()
data = 7
print(printRootToNodePath(root, data))
