"""   
Pair sum in array
Send Feedback
You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.
Note:
Given array/list can contain duplicate elements. 
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'num'.
Output format :
For each test case, print the total number of pairs present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^4
0 <= num <= 10^9

Time Limit: 1 sec
Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7
Sample Input 2:
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10
Sample Output 2:
0
2


 Explanation for Input 2:
Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.

For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).

"""
from sys import stdin


def pairSum(arr, n, num):
    arr.sort()
    count = 0
    left = 0
    right = n - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == num:
            if arr[left] == arr[right]:
                # If both numbers are the same, calculate the number of pairs using combinations
                print(arr[left])
                count += right - left + 1
                break
            else:
                left_count = 1
                right_count = 1
                left += 1
                right -= 1

                # Count the number of same elements on the left side
                while left < n and arr[left] == arr[left - 1]:
                    left_count += 1
                    left += 1

                # Count the number of same elements on the right side
                while right >= 0 and arr[right] == arr[right + 1]:
                    right_count += 1
                    right -= 1

                # Add the product of counts to the total count
                count += left_count * right_count
        elif currentSum < num:
            left += 1
        else:
            right -= 1
    return count


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# Main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))
    t -= 1
