""" 
Print Levelwise
Send Feedback
Given a generic tree, print the input tree in level wise order.
For printing a node with data N, you need to follow the exact format -
N:x1,x2,x3,...,xn
where, N is data of any node present in the generic tree. x1, x2, x3, ...., xn are the children of node N. Note that there is no space in between.
You need to print all nodes in the level order form in different lines.
Input format :
The first line of input contains data of the nodes of the tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.
Output Format :
The first and only line of output contains the elements of the tree in level wise order, as described in the task.
Constraints:
Time Limit: 1 sec
0 <= Data of a node <= 10^5
Sample Input 1:
10 3 20 30 40 2 40 50 0 0 0 0 


Sample Output 1:
10:20,30,40
20:40,50
30:
40:
40:
50:
"""
import sys
import queue


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def printLevelWiseTree(tree):
    if not tree:
        return

    q = queue.Queue()
    q.put(tree)
    # while not q.empty():
    #     current_node = q.get()
    #     children_str = ','.join(str(child.data) for child in current_node.children)
    #     print(current_node.data,":",children_str)

    #     for child in current_node.children:
    #         q.put(child)
    while not q.empty():
        ele = q.get()
        print(ele.data, end=":")
        printStr = ",".join(str(child.data) for child in ele.children)
        print(printStr)
        for el in ele.children:
            q.put(el)


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(" "))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
