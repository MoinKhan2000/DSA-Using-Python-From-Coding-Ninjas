def findMaxSubarray(nums):
    maxSum = float("-inf")

    def backTrack(start, currSum):
        nonlocal maxSum
        if currSum > maxSum:
            maxSum = currSum
        if start == len(nums):
            return
        for i in range(start, len(nums)):
            currSum += nums[i]
            backTrack(i + 1, currSum)
            currSum -= nums[i]

    backTrack(0, 0)
    return maxSum


arr = [1, 2, 3, 10]
print(findMaxSubarray(arr))
