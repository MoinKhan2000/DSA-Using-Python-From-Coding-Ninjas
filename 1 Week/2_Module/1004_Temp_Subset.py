def subsetRecursive(string, output):
    if len(string) == 0:
        print(output)
        return 1
    output1 = output
    output2 = output
    output2 += string[0]
    string = string[1:]
    subsetRecursive(string, output1)
    subsetRecursive(string, output2)


str = "123"
subsetRecursive(str, "")
