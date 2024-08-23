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


b1 = BTree(20)
b2 = BTree(10)
b3 = BTree(30)
b4 = BTree(50)
b5 = BTree(5)
b6 = BTree(15)
b7 = BTree(25)
b8 = BTree(31)
b9 = BTree(35)
b10 = BTree(45)
b11 = BTree(55)
b12 = BTree(65)

b1.left = b2
b1.right = b3

b1.left = b2
b1.right = b3

b2.left = b4
b2.right = b5

b3.left = b6
b3.right = b7

b4.left = b8
b4.right = b9

b5.left = b10
b5.right = b11

b6.left = b12

printBTreeAdvance(b1)
printBTree(b1)
