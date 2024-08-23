# Space complexity is maximum space required at any point of time.

"""
i = 0
n = int(input())
while i <= n:
    print(i)
    i += 1
"""

# Big O(1)

i = 0
n = int(input())
while i <= n:
    j = 0
    print(id(j))
    i += 1
"""
Here once J is created then it will use previous J Only. It doesn't require the previous J to run the program So the time complexity is O(1)
"""

# Note : Don't count the input space required in your space complexity.
# If the input arr is of n size which is to be sorted by the function and the function takes an input of len n and just compare with each and every element and sorts the array without making new array then O(1) will be the time complexity even though it is taking some constant space for the comparison. But if the function makes an second array for sorting of n lenth then it's space complexity will be O(n)


# Recursion takes space
