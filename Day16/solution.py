def checkValidString(s):
    if not s or s == "":
        return True
    stack = []
    for i in s:
        if i == "(" or i == "*":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                return False
    stack = []
    for t in range(len(s)-1,-1,-1):
        i = s[t]
        if i == ")" or i == "*":
            stack.append(i)
        elif i == "(":
            if stack:
                stack.pop()
            else:
                return False
    return True



s = "(((*)))))"
print(checkValidString(s))