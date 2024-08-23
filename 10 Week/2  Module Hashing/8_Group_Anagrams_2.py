def calculateFreqArr(word):
    freqArr = [0] * 26
    for i in word:
        freqArr[ord(i) % 97] += 1
    return freqArr


def calculateHashString(freqList):
    freq = [str(el) for el in freqList]
    return "$".join(freq)


def groupAnagrams(lst):
    ans = []
    hashTable = {}
    for word in lst:
        key = calculateHashString(calculateFreqArr(word))
        if key not in hashTable.keys():
            hashTable[key] = [word]
        else:
            hashTable[key].append(word)
    for el in hashTable.values():
        ans.append(el)
    return sorted(ans, key=lambda x: (len(x), x))


ans = groupAnagrams(["aaa", "abc", "bca", "cab", "bbca", "cabb", "ca"])
print(ans)
