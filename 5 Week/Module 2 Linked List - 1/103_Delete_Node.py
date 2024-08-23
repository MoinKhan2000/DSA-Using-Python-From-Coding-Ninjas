from sys import stdin
import sys


# Following is the Node class already written for the Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, pos):
    # Write your code here.
    i = 0
    curElem = head
    while curElem is not None:
        if pos == 0:
            head = head.next
            break
        elif curElem.next is None and pos - 1 == i:
            curElem = None
            break
        elif i == pos - 1:
            curElem.next = curElem.next.next
        curElem = curElem.next
        i = i + 1
    printLinkedList(head)
    print()


# Taking Input Using Fast I/O.
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


# To print the linked list.
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    # print()


# Main.
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
sys.exit()
