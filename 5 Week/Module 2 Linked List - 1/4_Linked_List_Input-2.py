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
    arr = [int(x) for x in input().split()]
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


# head = takeInputMyApproach()
head = takeInputBySir()
printLL(head)
