""" 
Pair sum to 0
Send Feedback
Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.


Note:
Array A can contain duplicate elements as well.
Input format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output format :
The first and only line of output contains the count of pair of elements in the array which sum up to 0. 
Constraints :
0 <= N <= 10^4
Time Limit: 1 sec
Sample Input 1:
5
2 1 -2 2 3
Sample Output 1:
2
Explanation
(2,-2) , (-2,2) will result in 0 , so the answer for the above problem is 2.
"""
from sys import stdin


def pairSum0(l, n):
    dictionary = {}
    for el in l:
        if el not in dictionary:
            dictionary[el] = 1
        else:
            dictionary[el] += 1
    total = 0
    for el in dictionary.keys():
        if dictionary[el] > 0:
            positivePair = dictionary.get(el, None)
            negativePair = dictionary.get(-el, None)
            if positivePair and negativePair:
                total += positivePair * negativePair
            elif positivePair or negativePair:
                total += positivePair if positivePair else negativePair
    return total // 2


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
print(pairSum0(arr, n))
