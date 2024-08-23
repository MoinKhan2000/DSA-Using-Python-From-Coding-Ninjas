""" 
Kth largest element
Send Feedback
Given an array 'arr' of random integers and an integer 'k', return the kth largest element in the array.


Note: Try to do this in O(n*log k) time.


Example:
Input:
5
3 2 5 1 4
2
Output:
4
Explanation:
Array in non increasing form is [5,4,3,2,1]. So the 2nd largest is 4.
Input Format :
The first line of input contains an integer 'n', that denotes the size of the array.
The next line contains 'n' space separated integers, that denote the value of the elements of the array 'arr'.
The next line contains an integer, that denotes the value of 'k'.
Output Format :
The output contains the kth largest element.
Sample Input 1 :
6
9 4 8 7 11 3
2
Sample Output 1 :
9
Explanation of sample input 1:
arr = [9,4,8,7,11,3]
Array 'arr' in non increasing form is [11,9,8,7,4,3]. So the 2nd largest is 9.
Sample Input 2 :
8
2 6 10 11 13 4 1 20
4
Sample Output 2 :
10
Constraints :
1 <= n <= 10^5
1 <= arr[i] <= 10^5
1 <= k <= n
Time Limit: 1 sec
"""
import heapq


def kthLargest(lst, k):
    output = lst[:k]
    heapq.heapify(output)
    for el in lst[k:]:
        if output[0] < el:
            heapq.heapreplace(output, el)
        # print(output)
    return output[0]


# Main
n = int(input())
lst = list(int(i) for i in input().strip().split(" "))
k = int(input())
ans = kthLargest(lst, k)
print(ans)
