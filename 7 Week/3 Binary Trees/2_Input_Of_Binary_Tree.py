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


def inputBTree():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BTree(rootData)
    root.left = inputBTree()
    root.right = inputBTree()
    return root


root = inputBTree()
printBTreeAdvance(root)
""" 
50
10
50
31
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
50 : Left : 10 , Right : 30
10 : Left : 50 , Right : 5
50 : Left : 31 , Right : 35
31 :
35 :
5 : Left : 45 , Right : 55
45 :
55 :
30 : Left : 15 , Right : 25
15 : Left : 65 ,
65 :
25 :


                50
                /\
              10  30
             /  \
            50  5
            /\
          31  35

"""