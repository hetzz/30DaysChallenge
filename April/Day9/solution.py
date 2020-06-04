def backspaceCompare(S,T):
    s = ""
    t = ""
    for i in range(len(T)):
        if T[i] == "#":
            t = t[:-1]
        else :
            t = t + T[i]

    for i in range(len(S)):
        if S[i] == "#":
            s = s[:-1]
        else :
            s = s + S[i]

    return s == t

S = "a##c"
T = "#a#c"
print(backspaceCompare(S,T))