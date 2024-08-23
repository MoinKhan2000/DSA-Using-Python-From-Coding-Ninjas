""" 
Reverse LL (Iterative)
Send Feedback
Given a singly linked list of integers, reverse it iteratively and return the head to the modified list.
 Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a separate line.
 Constraints :
1 <= t <= 10^2
0 <= N <= 10^4
Where N is the size of the singly linked list.

Time Limit: 1 sec
Sample Input 1 :
1
1 2 3 4 5 6 7 8 -1
Sample Output 1 :
8 7 6 5 4 3 2 1
Sample Input 2 :
2
10 -1
10 20 30 40 50 -1
Sample Output 2 :
10 
50 40 30 20 10 
Explanation to Sample Case 2 :
The first element after reversing is '10'. The next node of this node would be '50' which is the last node before
The original LinkedList is 1->10->20->30->40->50->NULL . After reversing , we
get 10<-10->20<-20->30<-30->40<-40->50<-5

"""

import sys
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedListIteratively(head):
    if head is None or head.next is None:
        return head
    prev = None
    current = head
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev


# Taking Input Using Fast I/O
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


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    head = reverseLinkedListIteratively(head)
    printLinkedList(head)
    t -= 1
sys.exit()
