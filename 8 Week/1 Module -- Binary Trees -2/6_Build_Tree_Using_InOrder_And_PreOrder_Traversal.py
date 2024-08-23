import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    print(root.data, end="")
    print(":L:", end="")
    print(root.left.data, end="") if root.left else print(-1, end="")
    print(",R:", end="")
    print(root.right.data) if root.right else print(-1)
    q = queue.Queue()
    q.put(root.left)
    q.put(root.right)
    while not q.empty():
        node = q.get()
        if not node:
            continue
        print(node.data, end="")
        print(":L:", end="")
        print(node.left.data, end="") if node.left else print(-1, end="")
        print(",R:", end="")
        print(node.right.data) if node.right else print(-1)
        q.put(node.left) if node.left else None
        q.put(node.right) if node.right else None


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


def buildTreeUsingInorderAndPreOrder(pre, inorder):
    if len(pre) == 1:
        node = BinaryTree(pre[0])
        return node
    rootData = pre[0]
    root = BinaryTree(rootData)
    rootIndexInInorder = -1
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return

    leftInOrder = inorder[0:rootIndexInInorder]
    rightInOrder = inorder[rootIndexInInorder + 1 :]
    lenLeftSubtree = len(leftInOrder)
    leftPreorder = pre[1 : lenLeftSubtree + 1]
    rightPreorder = pre[lenLeftSubtree + 1 :]
    root.left = buildTreeUsingInorderAndPreOrder(leftPreorder, leftInOrder)
    root.right = buildTreeUsingInorderAndPreOrder(rightPreorder, rightInOrder)

    return root


# root = takeInputLevelWise()
pre = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
root = buildTreeUsingInorderAndPreOrder(pre, inorder)
printLevelWise(root)
