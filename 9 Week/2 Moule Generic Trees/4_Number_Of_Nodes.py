class GenericTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def takeInputRecursive():
    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return None
    root = GenericTreeNode(rootData)
    nChildren = int(input(f"Enter number of childrens for {root.data} "))
    for i in range(nChildren):
        nodeChild = takeInputRecursive()
        root.children.append(nodeChild)
    return root


def printGenericTreeAdvance(node):
    if node == None:
        return
    print(node.data, " : ", end="")
    for child in node.children:
        print(child.data, ",", end="")
    print()
    for child in node.children:
        printGenericTreeAdvance(child)


def numberOfNodes(root):
    if root is None:
        return 0
    count = 1
    for child in root.children:
        count += numberOfNodes(child)
    return count


root = takeInputRecursive()
printGenericTreeAdvance(root)
numNodes = numberOfNodes(root)
print(numNodes)
