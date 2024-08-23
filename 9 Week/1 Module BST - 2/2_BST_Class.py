class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def isPresent(self, data):
        def isPresentHelper(root, data):
            if root is None:
                return None
            if root.data == data:
                return True
            if root.data > data:
                # Calling on the left
                return isPresentHelper(root.left, data)
            else:
                # Calling on the right
                return isPresentHelper(root.right, data)

        return isPresentHelper(self.root, data)

    def insert(self, data):
        self.numNodes += 1

        def insertNodeHelper(root, data):
            if root is None:
                node = BinaryTreeNode(data)
                return node
            if root.data > data:
                root.left = insertNodeHelper(root.left, data)
                return root
            else:
                root.right = insertNodeHelper(root.right, data)
                return root

        temp = insertNodeHelper(self.root, data)
        if temp is not None:
            self.root = temp
        else:
            self.root = self.root

    def deleteData(self, data):
        def findMinValueNode(root):  
            while root.left is not None:
                root = root.left
            return root.data

        def deleteDataHelper(root, data):
            # root is none
            if root is None:
                return False, None
            # if root.data is less than data then checking at the right
            if root.data < data:
                deleted, root.right = deleteDataHelper(root.right, data)
            # If root.data > data then checking at the left child
            elif root.data > data:
                deleted, root.left = deleteDataHelper(root.left, data)
            # Means got the node to be deleted
            else:
                # root is leaf node
                if root.right is None and root.left is None:
                    return True, None
                # root has only one child (left child only so making it root node )
                elif root.right is None:
                    return True, root.left
                # root has only one child (right child only so making it root node )
                elif root.left is None:
                    return True, root.right
                # means there are two child so handling it
                else:
                    # finding the minValue of the root.right child 
                    minVal = findMinValueNode(root.right)
                    # Changing the root.data to the minValue(root.right)
                    root.data = minVal
                    # Deleting taht minValue from root.right
                    deleted, root.right = deleteDataHelper(root.right, minVal)
                    # Returning True as we have got the element and deleted successfully with it's root
                    return True, root
            return deleted, root

        deleted, self.root = deleteDataHelper(self.root, data)
        if deleted:
            self.numNodes -= 1

    def printTree(self):
        def printTreeHelper(root):
            if root is None:
                return
            print(root.data, end=":")
            if root.left:
                print("L:", root.left.data, end=",")
            # else:
            #     print("L:", end="")
            if root.right:
                print("R:", root.right.data, end="")
            # else:
            #     print("R:", end="")
            print()
            printTreeHelper(root.left)
            printTreeHelper(root.right)

        printTreeHelper(self.root)

    def count(self):
        return self.numNodes


b = BST()
b.insert(10)
b.insert(23)
b.insert(23)
b.insert(223453)
b.insert(22353)
# print(b.count)
print(b.isPresent(23))
b.printTree()
print(b.count())
b.deleteData(23)
b.deleteData(23)
print(b.count())
b.printTree()
