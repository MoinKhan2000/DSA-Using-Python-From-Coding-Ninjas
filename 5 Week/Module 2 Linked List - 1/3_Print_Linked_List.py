class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


# O(n^2) - Time Complexity
def takeInput():
    arr = [int(x) for x in input().split(" ")]
    head = None
    for el in arr:
        if el == -1:
            break
        newNode = Node(el)
        if head is None:
            head = newNode
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = newNode
    return head


def printLL(head):
    current = head
    while current != None:
        print(current.data, end=" --> ")
        current = current.next
    print("None")


head = takeInput()
printLL(head)
