def groupAnagrams(lst):
    dictionary = {}
    freq = {}
    for el in lst:
        chars = [0] * 25
        for chr in el:
            ind = ord(chr) % 97
            chars[ind] += 1
        string = ""
        for chr in chars:
            string += str(chr) + "$"
        dictionary[el] = string
        if string in freq:
            freq[string].append([el])
        else:
            freq[string] = [[el]]

    arr = list()
    for key in freq:
        arr.append(freq[key])
    return arr


lst = ["abc", "aaa", "abbc", "cba", "bacb"]
arr = groupAnagrams(lst)
print()
for el in arr:
    for item in el:
        for i in item:
            print(i, end=" ")
    print()
