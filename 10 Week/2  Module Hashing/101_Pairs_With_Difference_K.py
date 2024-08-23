""" 
Pairs with Difference K
Send Feedback
You are given with an array of integers and an integer K. You have to find and print the count of all such pairs which have difference K.
Note: Take absolute difference between the elements of the array.
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol n.
The following line contains n space separated integers, that denote the value of the elements of the array.
The following line contains an integer, that denotes the value of K.
Output format :
The first and only line of output contains count of all such pairs which have an absolute difference of K. 
Constraints :
0 <= n <= 10^4
Time Limit: 1 sec
Sample Input 1 :
4 
5 1 2 4
3
Sample Output 1 :
2
Explanation
(5,2) and (1,4) are the possible combinations as their absolute difference is 3.
Sample Input 2 :
4
4 4 4 4 
0
Sample Output 2 :
6
"""


def printPairDiffK(l, k):
    freq = {}
    res = 0
    for elem in l:
        res += freq.get(elem - k, 0)
        res += freq.get(elem + k, 0)
        freq[elem] = freq.get(elem, 0) + 1
    if k != 0:
        return res
    return res


from collections import Counter


def countPairsWithDifferenceK(arr, n, K):
    freq = {}
    count = 0
    for num in arr:
        # Calculate the potential values for the pair
        diff1 = num - K
        diff2 = num + K

        # Check for the potential values in the frequency dictionary
        if diff1 in freq:
            count += freq[diff1]
        if diff2 in freq:
            count += freq[diff2]

        # Update the frequency dictionary
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    if K == 0:
        return count // 2
    return count


# Main
n = int(input())
arr = list(map(int, input().strip().split(" ")))
K = int(input())

result = countPairsWithDifferenceK(arr, n, K)
print(result)
