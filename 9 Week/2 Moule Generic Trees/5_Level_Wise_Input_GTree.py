import queue


class GenericTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def takeLevelWiseInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = GenericTreeNode(rootData)
    q.put((root))
    while not q.empty():
        current_node = q.get()
        print("Enter num of children for ", current_node.data)
        noOfChildren = int(input())
        for i in range(noOfChildren):
            childData = int(input())
            if childData != -1:
                newChild = GenericTreeNode(childData)
                current_node.children.append(newChild)
                q.put(newChild)
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


root = takeLevelWiseInput()
printGenericTreeAdvance(root)


""" 

Enter root
1
Enter num of children for  1
3
2
3
4
Enter num of children for  2
0
Enter num of children for  3
2
5
6
Enter num of children for  4
0
Enter num of children for  5
0
Enter num of children for  6
3
7
8
9
Enter num of children for  7
0
Enter num of children for  8
0
Enter num of children for  9
0
1  : 2 ,3 ,4 ,
2  :
3  : 5 ,6 ,
5  :
6  : 7 ,8 ,9 ,
7  :
8  :
9  :
4  :

"""
