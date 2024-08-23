""" 
Triplet sum
Send Feedback
You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.
Note :
Given array/list can contain duplicate elements.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
Output format :
For each test case, print the total number of triplets present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= X <= 10^9

Time Limit: 1 sec
Sample Input 1:
1
7
1 2 3 4 5 6 7 
12
Sample Output 1:
5
Sample Input 2:
2
7
1 2 3 4 5 6 7 
19
9
2 -5 8 -6 0 5 10 11 -3
10
Sample Output 2:
0
5


 Explanation for Input 2:
Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)

"""

import sys


def pairSum(arr, n, num):
    arr.sort()
    count = 0
    left = 0
    right = n - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == num:
            print(arr[left], arr[right])
            if arr[left] == arr[right]:
                count += (right - left + 1) * (right - left) // 2
                break
            else:
                left_count = 1
                right_count = 1
                left += 1
                right -= 1

                while left < n and arr[left] == arr[left - 1]:
                    left_count += 1
                    left += 1

                while right >= 0 and arr[right] == arr[right + 1]:
                    right_count += 1
                    right -= 1

                count += left_count * right_count
        elif currentSum < num:
            left += 1
        else:
            right -= 1
    return count


def tripletSum(arr, n, X):
    arr.sort()
    count = 0
    for i in range(n - 2):
        currentSum = X - arr[i]
        count += pairSum(
            arr[1 + i :], len(arr[i + 1 :]), currentSum
        )  # Corrected n to len(arr)

    # print(count)  # Add a print statement to display the count


t = int(input())
while t > 0:
    n = int(input())
    if n > 0:
        arr = list(map(int, input().split()))
        X = int(input())
        tripletSum(arr, n, X)
        t -= 1
    else:
        print("0")
