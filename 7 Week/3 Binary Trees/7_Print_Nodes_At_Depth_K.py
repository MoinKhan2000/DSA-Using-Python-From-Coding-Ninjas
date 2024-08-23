class BTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inputBTree():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BTree(rootData)
    root.left = inputBTree()
    root.right = inputBTree()
    return root


def printNodesAtDepthK(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    printNodesAtDepthK(root.left, k - 1)
    printNodesAtDepthK(root.right, k - 1)
    return


def printNodeAtDepthAssumeYouAreAtDepthD(root, k, d=0):
    if not root:
        return
    if k == d:
        print(root.data)
        return
    printNodeAtDepthAssumeYouAreAtDepthD(root.left, k, d + 1)
    printNodeAtDepthAssumeYouAreAtDepthD(root.right, k, d + 1)


root = inputBTree()
n = int(input())
print("PrintNodesAtDepthK , n = ", n)
printNodesAtDepthK(root, n)
printNodeAtDepthAssumeYouAreAtDepthD(root, 2, 0)
