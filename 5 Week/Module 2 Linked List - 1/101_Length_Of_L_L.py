"""  
Length of LL
Send Feedback
Given the head of a singly linked list of integers, find and return its length.

Example:
Sample Linked List
    5->4->12->7->Null
    ^
    |
    Head 

The length of the list is 4. Hence we return 4.

Note:
Exercise caution when dealing with edge cases, such as when the head is NULL. Failing to handle these edge cases appropriately may result in a runtime error in your code.


Input format :
The first and only line contains elements of the singly linked list separated by a single space, -1 indicates the end of the singly linked list and hence, would never be a list element.


Output format :
Return a single integer denoting the length of the linked list.
Sample Input 1 :
3 4 5 2 6 1 9 -1


Sample Output 1 :
7


Explanation of sample input 1 :
The number of nodes in the given linked list is 7.
Hence we return 7.


Sample Input 2 :
10 76 39 -3 2 9 -23 9 -1

Sample Output 2 :
8


Expected Time Complexity:
Try to do this in O(n).


 Constraints :
0 <= N <= 10^5
Time Limit: 1 sec

"""


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


def takeInput():
    arr = [int(x) for x in input().split(" ")]
    head = None
    number = 0
    for el in arr:
        if el == -1:
            break
        number += 1
        newNode = Node(el)
        if head is None:
            head = newNode
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = newNode
    return number


lengthOfLL = takeInput()
print(lengthOfLL)
