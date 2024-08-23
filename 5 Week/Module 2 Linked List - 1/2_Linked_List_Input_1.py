class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


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


head = takeInput()
while head is not None:
    print(str(head.data) + "->", end="")
    head = head.next

print("None")
