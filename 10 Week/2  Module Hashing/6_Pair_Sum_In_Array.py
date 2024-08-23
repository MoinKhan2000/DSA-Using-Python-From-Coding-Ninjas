def pairSumInArray(arr, k):
    dictionary = {}
    ans = 0
    for i in range(len(arr)):
        val = k - arr[i]
        ans += dictionary.get(val, 0)
        if arr[i] not in dictionary:
            dictionary[arr[i]] = 1
        else:
            dictionary[arr[i]] += 1
    print(dictionary)
    return ans


# def pairSumInArray(arr, k):
#     freq = {}
#     ans = 0
#     for el in arr:
#         expect = k - el
#         ans += freq.get(expect, 0)
#         if el in freq.keys():
#             freq[el] += 1
#         else:
#             freq[el] = 1
#     return ans
# print(freq)
# return ans


A = [2, 1, 3, 4, 2, 3, 5, 6, 1, 2]
K = 4
""" 
total 7 ways of pair which sum to 4
2,2
2,2
2,2
1,3
3,1
1,3
3,1
"""
print(pairSumInArray(A, K))
