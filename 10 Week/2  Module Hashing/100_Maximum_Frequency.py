"""  
Maximum Frequency
Send Feedback
You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.
If two or more elements are having the maximum frequency, return the element which occurs in the array first.
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output Format :
The first and only line of output contains most frequent element in the given array.
Constraints:
0 <= N <= 10^8
Time Limit: 1 sec
Sample Input 1 :
13
2 12 2 11 12 2 1 2 2 11 12 2 6 
Sample Output 1 :
2
Sample Input 2 :
6
7 2 2 4 8 4
Sample Output 2 :
2
Explanation:
Here, both element '2' and element '4' have same frequency but '2' ocurr first in orignal array that's why we are returning '2' as output. 
"""

import sys
def maxRepeating(arr, k):
    freq = [0] * k
    maxElem = -1
    maxFreq = -1

    for el in arr:
        freq[el] += 1

        if freq[el] > maxFreq or (freq[el] == maxFreq and el < maxElem):
            maxFreq = freq[el]
            maxElem = el

    return maxElem


def returnWordsWithFrequencyK(lst):
    freq = {}
    for el in lst:  
        if el not in freq.keys():
            freq[el] = 1
        elif el in freq.keys():
            freq[el] += 1
    maxElem = -1
    maxFreq = -1
    for item in freq:
        print(item, freq[item])
    for el in lst:
        if freq[el] >= maxFreq:
            maxFreq = freq[el]
            maxElem = el

    return maxElem


len = int(input())
lst = [int(x) for x in input().split()]
# print(returnWordsWithFrequencyK(lst))
print(maxRepeating(lst, 3))
