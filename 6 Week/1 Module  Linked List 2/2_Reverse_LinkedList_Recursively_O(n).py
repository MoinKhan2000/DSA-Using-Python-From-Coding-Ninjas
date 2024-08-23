import sys
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# T(n) = T(n-1)+n-1     -- O(n^2)
def reverseLinkedListRecAdvanced(head):
    if head is None or head.next is None:
        return head, head
    smallHead, smallTail = reverseLinkedListRecAdvanced(head.next)
    smallTail.next = head
    head.next = None
    return smallHead, head


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

    newHead, head = reverseLinkedListRecAdvanced(head)
    printLinkedList(newHead)

    t -= 1

sys.exit()
