import sys
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# T(n) = K+n-1     -- O(n)
def reverseLLExtraOrdinay(head):
    if head is None or head.next is None:
        return head

    smallHead = reverseLLExtraOrdinay(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead


# Taking Input Using Fast I/O
def takeInput():
    head = None
    smallTail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            smallTail = newNode

        else:
            smallTail.next = newNode
            smallTail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()

    head = reverseLLExtraOrdinay(head)
    printLinkedList(head)

    t -= 1

sys.exit()
