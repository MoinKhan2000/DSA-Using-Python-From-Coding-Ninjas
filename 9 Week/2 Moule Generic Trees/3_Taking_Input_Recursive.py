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


root = takeInputRecursive()
printGenericTreeAdvance(root)


"""  
Enter root Data
5
Enter number of childrens for 5 4
Enter root Data
2
Enter number of childrens for 2 -1
Enter root Data
9
Enter number of childrens for 9 2
Enter root Data
15
Enter number of childrens for 15 -1
Enter root Data
1
Enter number of childrens for 1 -1
Enter root Data
8
Enter number of childrens for 8 -1
Enter root Data
7
Enter number of childrens for 7 -1
5  : 2 ,9 ,8 ,7 ,
2  :
9  : 15 ,1 ,
15  :
1  :
8  :
7  :
"""


"""  
Enter root Data
5
Enter number of childrens for 5 4
Enter root Data
2
Enter number of childrens for 2 0
Enter root Data
9
Enter number of childrens for 9 2
Enter root Data
15
Enter number of childrens for 15 0
Enter root Data
1
Enter number of childrens for 1 0
Enter root Data
8
Enter number of childrens for 8 0
Enter root Data
7
Enter number of childrens for 7 0
5  : 2 ,9 ,8 ,7 ,
2  :
9  : 15 ,1 ,
15  :
1  :
8  :
7  :
"""
