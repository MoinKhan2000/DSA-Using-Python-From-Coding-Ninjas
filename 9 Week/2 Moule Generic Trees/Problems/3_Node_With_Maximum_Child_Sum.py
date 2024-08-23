from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans


def maxSumNodeHelper(tree, ms=float("-inf"), msn=None):
    if tree is None:
        return ms, msn

    sum = tree.data
    for child in tree.children:
        cSum, _ = maxSumNodeHelper(child, ms, msn)
        sum += cSum

    if sum > ms:
        msn = tree.data
        ms = sum

    return ms, msn


# def maxSumNode(tree, ms=float("-inf"), msn=0):
#     if not tree:
#         return None
#     node = None
#     maxSum = 0
#     for elem in tree.children:
#         ms, msn = maxSumNodeHelper(elem, ms, msn)
#         if ms > maxSum:
#             maxSum = ms
#             node = elem
#     return node.data

msn = 0
ms = float("-inf")


def maxSumNode(tree):
    global msn, ms
    sum = 0
    if tree is None:
        return 0, 0
    for child in tree.children:
        csum = child.data
        sum += csum
    sum += tree.data
    if sum > ms:
        ms = sum
        msn = tree.data

    for child in tree.children:
        csum = maxSumNode(child)
        print(csum)
        if csum > ms:
            ms = csum
            msn = tree.data
    return sum

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
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
# print(temp)
print(maxSumNode(tree))
print("maximum sum node",msn)
print(ms)
