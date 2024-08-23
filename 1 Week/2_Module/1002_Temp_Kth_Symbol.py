"""
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        mid = (1 << (N - 1)) // 2
        if K <= mid:
            return int(self.kthGrammar(N - 1, K))

        else:
            return int( self.kthGrammar(N - 1, K - mid))


# Example usage
n = int(input())
k = int(input())
solution = Solution()
print(int(solution.kthGrammar(n, k)))
"""

import sys


def kth_symbol(N, K):
    if N == 1 and K == 1:
        return 1
    mid = (pow(2, N - 1)) // 2
    if K <= mid:
        return kth_symbol(N - 1, K)
    else:
        return not kth_symbol(N - 1, K - mid)


num = int(input())
for i in range(0, num):
    n, k = [int(x) for x in input().split(" ")]
    print(int(kth_symbol(n, k)))

sys.exit()
