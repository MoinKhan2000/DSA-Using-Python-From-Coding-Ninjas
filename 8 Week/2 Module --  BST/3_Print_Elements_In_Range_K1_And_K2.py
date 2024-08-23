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


def elementsInRangeK1K2(root, k1, k2):
    if root is None:
        return
    if root.data > k2:
        elementsInRangeK1K2(root.left, k1, k2)
    elif root.data < k1:
        elementsInRangeK1K2(root.right, k1, k2)
    else:
        print(root.data)
        elementsInRangeK1K2(root.left, k1, k2)
        elementsInRangeK1K2(root.right, k1, k2) 


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
# print(searchNodeInBST(root, n))
elementsInRangeK1K2(root, 4, 10)
