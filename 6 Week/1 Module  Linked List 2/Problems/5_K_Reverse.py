""" 
kReverse
Send Feedback
Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
 'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.
Example :
Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4
 Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

The second line of input contains a single integer depicting the value of 'k'.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.
0 <= k <= M

Time Limit:  1sec
Sample Input 1 :
1
1 2 3 4 5 6 7 8 9 10 -1
4
Sample Output 1 :
4 3 2 1 8 7 6 5 10 9
Sample Input 2 :
2
1 2 3 4 5 -1
0
10 20 30 40 -1
4
Sample Output 2 :
1 2 3 4 5 
40 30 20 10 

"""


# remaining = head.next.next.next
# head, oldHead = reverseLinkedListIteratively(head, head.next.next.next)
# oldHead.next = remaining
# return head
from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedListIteratively(head, end):
    if head is None:
        return head
    prev = None
    current = head
    while current != end:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev, head


def lenOfList(head):
    curElem = head
    i = 0
    while curElem is not None:
        curElem = curElem.next
        i = i + 1
    return i


def kReverse(head, k):
    # return reverseLinkedListIteratively(head,head.next.next)[0]
    if head is None or head.next is None or k <= 1:
        return head
    start = head
    end = head
    i = 0
    curElem = head
    while curElem and i < k:
        if end is None:
            return head
        i += 1
        end = end.next
        curElem = curElem.next

    # printLinkedList(end)
    remaining = end
    end, start = reverseLinkedListIteratively(start, end)
    start.next = kReverse(remaining, k)
    return end


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = [int(x) for x in input().split()]
    if datas is None:
        return

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


# main
# t = int(stdin.readline().rstrip())
# while t > 0:
num = int(input())
head = takeInput()
k = int(stdin.readline().strip())

newHead = kReverse(head, k)
printLinkedList(newHead)

    # t -= 1
