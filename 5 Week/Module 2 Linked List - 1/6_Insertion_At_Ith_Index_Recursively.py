class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


# My Own Approach
# def insertAtIndexRecursive(head, data, index):
#     if head is None:
#         return
#     if index == 0:
#         node = Node(data)
#         node.next = head
#         head = node
#         return head
#     head.next = insertAtIndexRecursive(head.next, data, index - 1)
#     return head


# Sir Logic (Better as it handles negative indexes also)     Time Complexity is O(n)
def insertAtIndexRecursive(head, data, index):
    if index < 0:
        return head
    if index == 0:
        node = Node(data)
        node.next = head
        return node

    smallHead = insertAtIndexRecursive(head, data, index - 1)
    head.next = smallHead
    return head


def takeInputBySir():
    # arr = [1, 2, 23, -1]
    arr = [int(x) for x in input().split(" ")]
    head = None
    tail = None
    for el in arr:
        if head is None:
            node = Node(el)
            head = node
            tail = node
        else:
            node = Node(el)
            tail.next = node
            tail = node

    return head


def printLL(head):
    current = head
    while current != None:
        print(current.data, end=" --> ")
        current = current.next
    print("None")


def sizeLL(head):
    i = 0
    current = head
    while current is not None:
        current = current.next
        i += 1
    print(i)
    return i


head = takeInputBySir()
ele, index = [int(x) for x in input().split(" ")]
printLL(head)
head = insertAtIndexRecursive(head, ele, index)
printLL(head)
