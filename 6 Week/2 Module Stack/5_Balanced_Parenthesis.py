def isBalanced(string):
    s = []
    for char in string:
        if char in "({[":
            s.append(char)
        elif char == ")":
            if not s or s[-1] != "(":
                return False
            s.pop()
        elif char == "}":
            if not s or s[-1] != "{":
                return False
            s.pop()
        elif char == "]":
            if not s or s[-1] != "[":
                return False
            s.pop()
    return True if not s else False


string = input()
ans = isBalanced(string)
print(ans)
