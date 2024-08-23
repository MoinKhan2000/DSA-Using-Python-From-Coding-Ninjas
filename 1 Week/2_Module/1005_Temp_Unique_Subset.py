def subsetRecursive(string, output, setOfSubset):
    if len(string) == 0:
        setOfSubset = setOfSubset.append(output)
        return 1
    output1 = output
    output2 = output
    output2 += string[0]
    string = string[1:]
    subsetRecursive(string, output1, setOfSubset)
    subsetRecursive(string, output2, setOfSubset)
    return setOfSubset


# Print subSets / powerSet
str = "abc"
powerSet = []
powerSet = set(subsetRecursive(str, "", powerSet))
print(powerSet)
""" Power set === Print Subset """

# Print all subSequences
"""
string = "abc"
substrings = "a b c ab bc abc" (only substring) (Order matters)
subsequence = " a b c ab ac bc abc" (Order matters here);
subsets = " a b c ab ba ac bc ca abc bca" 

substring --> subsequence --> subset


subsequence = " , a b c ab bc ac abc "
subsequences = ["", ",","a ","b ","c ","ab ","bc ","ac ","abc "]
subsets=[ " ", a b c {ab,ba} {bc,cb} , {ac,ca}, {abc,acb,bac,cab,bca,cba} ]


Conclusion - If the question is given to print powerSet/ subsequence / subsets -> Do Only this one (this question)
"""

# Lexicogrpaphical -- "a ab abhishek azim bishwashan bheeshma Moin Nandi Oracle Pravin"
# print("Lexicographically sorted list")

