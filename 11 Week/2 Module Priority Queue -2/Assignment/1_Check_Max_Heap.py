""" 
Check Max-Heap
Send Feedback
Given an array of integers, check whether it represents max-heap or not. Return true if the given array represents max-heap, else return false.
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output Format :
The first and only line of output contains true if it represents max-heap and false if it is not a max-heap.
Constraints:
1 <= N <= 10^5
1 <= Ai <= 10^5
Time Limit: 1 sec
Sample Input 1:
8
42 20 18 6 14 11 9 4
Sample Output 1:
true
"""


def checkMaxHeap(lst, i=0):
    n = len(lst)
    if i >= n:
        return True
    root = lst[i]
    left_idx = 2 * i + 1
    right_idx = 2 * i + 2
    if left_idx < n and lst[left_idx] > root:
        return False
    if right_idx < n and lst[right_idx] > root:
        return False
    if not checkMaxHeap(lst, left_idx) or not checkMaxHeap(lst, right_idx):
        return False
    return True


# Main Code
n = int(input())
lst = list(int(i) for i in input().strip().split(" "))
print("true") if checkMaxHeap(lst) else print("false")
