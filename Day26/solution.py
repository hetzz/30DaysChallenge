def lcs(ptr1, ptr2, str1, str2):
    if ptr1 == len(str1) or ptr2 == len(str2):
        return 0
    elif str1[ptr1] == str2[ptr2]:
        return 1 + lcs(ptr1 +1, ptr2+1, str1, str2) 

    else:
        return max(lcs(ptr1+1, ptr2, str1, str2),lcs(ptr1, ptr2+1, str1, str2))

str1 = "ace"
str2 = "ajckle"
print(lcs(0,0,str1,str2))