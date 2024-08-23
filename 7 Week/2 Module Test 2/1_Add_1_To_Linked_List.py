## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
""" 
Next Number
Send Feedback
Given a large number represented in the form of a linked list. Write code to increment the number by 1 in-place(i.e. without using extra space).
Note: You don't need to print the elements, just update the elements and return the head of updated LL.
Input Constraints:
1 <= Length of Linked List <=10^6.
Input format :
Line 1 : Linked list elements (separated by space and terminated by -1)
Output Format :
Line 1: Updated linked list elements 
Sample Input 1 :
3 9 2 5 -1
Sample Output 1 :
3 9 2 6
Sample Input 2 :
9 9 9 -1
Sample Output 1 :
1 0 0 0 

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseList(head):
    if head is None or head.next is None:
        return head

    smallHead = reverseList(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead


# Not a clear approachy
def nextNumber(head):
    # Implement Your Code here
    head = reverseList(head)
    curr = head
    boolean = True
    while curr is not None and boolean:
        if curr.next == None and curr.data == 9:
            curr.data = 1
            newNode = Node(0)
            newNode.next = head
            head = newNode
            curr = curr.next
        elif curr.data == 9:
            curr.data = 0
            curr = curr.next
        else:
            curr.data = curr.data + 1
            curr = curr.next
            boolean = False
    head = reverseList(head)
    return head


def addOne(head):
    if head == None:
        return head
    head = reverseList(head)
    curr = head
    prev = None
    carry = 0
    while curr is not None:
        sum = 0
        if prev is None:
            sum = curr.data + 1
        else:
            sum = curr.data + carry
        carry = sum / 10
        curr.data = sum % 10
        prev = curr
        curr = curr.next

    if carry == 1:
        newNode = Node(1)
        prev.next = newNode

    return reverseList(head)


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    return


# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
# head = addOne(l)
printll(head)
