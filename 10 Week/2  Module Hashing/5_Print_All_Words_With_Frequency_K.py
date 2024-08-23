# We have to tell all the words those are repeating k times  in lst
def returnWordsWithFrequencyK(lst, k):
    freq = {}  # Using the dictionary as an predefined Hash table
    for el in lst:
        if el not in freq.keys():
            # freq[el] = 1
            freq.update([(el, 1)])
        elif el in freq.keys():
            freq[el] += 1
    result = []
    for keys in freq:
        if freq[keys] >= k:
            result.append(keys)
    return result


arr = [1, 2, 1, 3, 2, 4, 3, 5, 7, 4, 2]
k = 2
print(returnWordsWithFrequencyK(arr, k))
lst = ["cat", "dog", "cat", "elephant", "dog"]
print(returnWordsWithFrequencyK(lst, k))
