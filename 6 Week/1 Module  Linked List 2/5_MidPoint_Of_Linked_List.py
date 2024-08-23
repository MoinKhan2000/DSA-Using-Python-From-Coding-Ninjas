from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lenOfLL(head):
    if head is None:
        return -1
    i = 0
    while head.next is not None:
        i += 1
        head = head.next
    return i


def midPoint(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    mid = midPoint(head)

    if mid is not None:
        # printLinkedList(mid)
        print(mid.data)
    t -= 1
