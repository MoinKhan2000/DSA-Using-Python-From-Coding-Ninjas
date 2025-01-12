"""  
Matrix Chain Multiplication
Send Feedback
Given a chain of matrices A1, A2, A3,.....An. Your task is to find out the minimum cost to multiply these matrices. The cost of matrix multiplication is defined as the number of scalar multiplications. A Chain of matrices A1, A2, A3,.....An is represented by a sequence of numbers in an array ‘arr’ where the dimension of 1st matrix is equal to arr[0] * arr[1] , 2nd matrix is arr[1] * arr[2], and so on.
For example:
For arr[ ] = { 10, 20, 30, 40}, matrix A1 = [10 * 20], A2 = [20 * 30], A3 = [30 * 40]

Scalar multiplication of matrix with dimension 10 * 20 is equal to 200.
Input Format:
The first line of input contains an integer ‘T’, denoting the number of test cases. Then each test case follows.

The first line of each test case contains the Integer ‘N’ denoting the number of elements in the array.

The second and the last line of each test case contains ‘N’ single space-separated integers representing the elements of the array.
Output Format:
For each test case, print a single integer, denoting the minimum cost of matrix multiplication.

Output of each test case will be printed on a separate line.
Note:
You do not need to print anything, it has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 5
2 <= N <= 100
1 <= arr[i] <= 400 

Time Limit: 1 sec.
Sample Input 1:
2
4
4 5 3 2
4
10 15 20 25
Sample Output 1:
8000
70
Sample Output Explanation 1:
In the first test case, there are three matrices of dimensions A = [4 5], B = [5 3] and C = [3 2]. The most efficient order of multiplication is A * ( B * C).
Cost of ( B * C ) = 5 * 3 * 2 = 30  and (B * C) = [5 2] and A * (B * C) = [ 4 5] * [5 2] = 4 * 5 * 2 = 40. So the overall cost is equal to 30 + 40 =70.

In the second test case, there are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.

If we multiply in order- A1*(A2*A3), then the number of multiplications required is 11250.

If we multiply in order- (A1*A2)*A3, then the number of multiplications required is 8000.

Thus a minimum number of multiplications required is 8000. 
Sample Input 2:
1
4
1 4 3 2
Sample Output 2:
18
Explanation of Sample Output 2:
In the first test case, there are three matrices of dimensions A = [1 4], B = [4 3] and C = [3 2]. The most efficient order of multiplication is (A *  B) * C .

"""

from os import *
from sys import *
from collections import *
from math import *


def f(i, j, arr, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    minimum = 1e9
    for k in range(i, j):
        steps = arr[i - 1] * arr[k] * arr[j] + f(i, k, arr, dp) + f(k + 1, j, arr, dp)
        minimum = min(steps, minimum)
    dp[i][j] = minimum
    return dp[i][j]


def matrixMultiplication(arr, n):
    # Write your code here.
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return f(1, n - 1, arr, dp)
