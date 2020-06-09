def reverseString(s):
    l = len(s)
    for i in range(len(s)//2):
        s[i] , s[l-i-1] = s[l-i-1],s[i]

s = ["h","e","l","l","o"]
reverseString(s)
print(s)