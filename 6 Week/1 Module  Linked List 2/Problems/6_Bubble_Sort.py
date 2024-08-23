from sys import stdin


# Node class for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Bubble Sort function to sort the Linked List
def bubbleSort(head):
    if head is None:
        return head
    end = None
    while end != head:
        swapped = False
        p = head
        q = head.next
        while q != end:
            if q.data <= p.data:
                q.data, p.data = p.data, q.data
                swapped = True
            q = q.next
            p = p.next
        end = p
        if not swapped:
            break
    return head


# Function to take input and create the Linked List
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


# Function to print the Linked List
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Main program
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
