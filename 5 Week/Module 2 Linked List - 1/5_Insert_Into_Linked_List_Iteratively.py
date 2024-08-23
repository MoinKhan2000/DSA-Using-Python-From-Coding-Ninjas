class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


# O(n^2) -----> Reduced to O(n) - My Own Approach
def takeInputMyApproach():
    arr = [int(x) for x in input().split(" ")]
    head = None
    for i in range(len(arr) - 1, -1, -1):
        if i == len(arr) - 1:
            node = Node(arr[i])
            head = node
        else:
            node = Node(arr[i])
            node.next = head
            head = node
    return head


# O(n^2) -----> Reduced to O(n) - Sir Approach ( Better one )
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


def insertAtStart(head, data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head


def insertAtEnd(head, data):
    current = head
    while current.next is not None:
        current = current.next
    newNode = Node(data)
    current.next = newNode
    return head


# Using My Logic I built this function
# def insertAtIndex(head, data, index):
#     if index == 0:
#         return insertAtStart(head, data)
#     else:
#         i = 0
#         current = head
#         while current is not None:
#             if i == index - 1:
#                 newNode = Node(data)
#                 newNode.next = current.next
#                 current.next = newNode
#             i += 1
#             current = current.next
#         return head


def sizeLL(head):
    i = 0
    current = head
    while current is not None:
        current = current.next
        i += 1
    print(i)
    return i


# Sir Logic - Time Commplexity O(n)
def insertAtIndex(head, index, data):
    if index < 0 or index > sizeLL(head):
        return head
    i = 0
    current = head
    previous = None
    while i < index:
        previous = current
        current = current.next
        i += 1
    node = Node(data)
    if previous is not None:
        previous.next = node
    else:
        head = node
    node.next = current
    return head


# head = takeInputMyApproach()
#  arr = [1, 2 - 1]
# printLL(head)
# head = insertAtStart(head, 0)
# printLL(head)
# head = insertAtEnd(head, 1)
# printLL(head)
# printLL(head)
# head = insertAtIndex(head, 0, 0)
# printLL(head)

# head = insertAtIndex(head, 3, 0)
# printLL(head)

# head = insertAtIndex(head, 3, 2)
# printLL(head)

# head = insertAtIndex(head, 5, 5)
# printLL(head)

head = takeInputBySir()
index, ele = [int(x) for x in input().split(" ")]
printLL(head)
head = insertAtIndex(head, index, ele)
printLL(head)
